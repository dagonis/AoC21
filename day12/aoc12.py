connections = {}

def add_connection(src, dst):
    if dst != "start":
        connections[src] = connections.get(src, []) + [dst]


def find_paths(current_path, b):
    if 'end' in current_path:
        return [current_path]
    c = [(connection in current_path and connection.islower(), connection) for connection in connections[current_path[-1]]]
    return [l for x, connection in c if not(x & b) for l in find_paths(current_path+[connection], x|b)]

def main() -> None:
    with open('test.txt', 'r') as input_file:
        raw_caves = [_.rstrip() for _ in input_file]
    for cave in raw_caves:
        src, dst = cave.split('-')
        add_connection(src, dst)
        add_connection(dst, src)
    print(connections)
    res = u(['start'], 0)
    print(len(res))


if __name__ == '__main__':
    main()