from collections import deque
from dataclasses import dataclass
import itertools
from math import prod

global versions
versions = []

@dataclass
class Packet:
    version: int
    packet_type: int

@dataclass
class LiteralPacket(Packet):
    raw_payload: str

    @property
    def value(self):
        return int(self.raw_payload, 2)

    @property
    def bit_length(self):
        return 6 + len(self.raw_payload)


@dataclass
class OperatorPacket(Packet):
    len_type_id: int
    subpackets: list

    @property
    def bit_length(self):
        return 7 + sum([_.bit_length for _ in self.subpackets])

    @property
    def value(self):
        subpacket_values = [_.value for _ in self.subpackets]
        if self.packet_type == 0:
            return sum(subpacket_values)
        elif self.packet_type == 1:
            return prod(subpacket_values)
        elif self.packet_type == 2:
            return min(subpacket_values)
        elif self.packet_type == 3:
            return max(subpacket_values)
        elif self.packet_type == 5:
            a, b = [_.value for _ in self.subpackets]
            return 1 if a > b else 0
        elif self.packet_type == 3:
            a, b = [_.value for _ in self.subpackets]
            return 1 if a < b else 0
        elif self.packet_type == 5:
            a, b = [_.value for _ in self.subpackets]
            return 1 if a == b else 0

def read_n_bytes(number_of_bits, queue) -> str:
    return "".join([queue.popleft() for _ in range(number_of_bits)])

def parse_packets(bits):
    bit_queue = deque(bits)
    _packets = []
    while bit_queue and len(bit_queue) > 10:
        # print('working', bit_queue)
        version = int(read_n_bytes(3, bit_queue), 2)
        versions.append(version)
        packet_type = int(read_n_bytes(3, bit_queue), 2)
        if packet_type == 4:
            # Literal Packets
            payload_chunk = read_n_bytes(5, bit_queue)
            payload = ""
            while payload_chunk[0] == '1':
                payload += payload_chunk[1:]
                payload_chunk = read_n_bytes(5, bit_queue)
            else:
                payload += payload_chunk[1:]
            _packets.append(LiteralPacket(version, packet_type, payload))
        else:
            # Operator Packets, complete madness
            len_type_bit = int(read_n_bytes(1, bit_queue), 2)
            if len_type_bit == 0:
                subpacket_bits = int(read_n_bytes(15, bit_queue), 2)
                more_packets = parse_packets(read_n_bytes(subpacket_bits, bit_queue))
                _packets.append(OperatorPacket(version, packet_type, len_type_bit, more_packets))
            elif len_type_bit == 1:
                subpacket_num = int(read_n_bytes(11, bit_queue), 2)
                bit_queue_copy = bit_queue.copy()
                temp_subpackets = parse_packets(read_n_bytes(len(bit_queue_copy), bit_queue_copy))[:subpacket_num+1]
                subpacket_len = sum([_.bit_length for _ in temp_subpackets])
                subpacket_bits = read_n_bytes(subpacket_len, bit_queue)
                more_packets = parse_packets(subpacket_bits)
                _packets.append(OperatorPacket(version, packet_type, len_type_bit, more_packets))
    return _packets


def main() -> None:
    with open('input.txt', 'r') as input_file:
        packet = [_.strip() for _ in input_file][0]
    bits = ""
    for hexchar in list(packet):
        bits += f"{int(hexchar, 16):04b}"
    packets = parse_packets(bits)
    print(f'Part 1: {sum(versions)}')
    for p in packets:
        print(p.__dict__)
        print(p.value)
            



        

if __name__ == '__main__':
    main()