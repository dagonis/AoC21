from collections import defaultdict, deque
import heapq as heap
from typing import Dict, List, Tuple, TypeVar, Protocol
import heapq
from dataclasses import dataclass

@dataclass
class Map:
    grid: List

    def __post_init__(self) -> None:
        self.row_len = len(self.grid)
        self.col_len = len(self.grid[0])
        self.nodes = {}
        for row in range(0, self.row_len):
            for col in range(0, self.col_len):
                self.nodes[(row, col)] = Node((row, col), None, self.grid[row][col])

        # self.num_rows = self.num_grid_rows * repetitions
        # self.num_cols = self.num_grid_cols * repetitions
        # self.repetitions = repetitions

    def get_neighbors(self, position: Tuple) -> List:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        i, j = position
        result = []
        for dir in dirs:
            neighbor = [i + dir[0], j + dir[1]]
            if 0 <= neighbor[0] < self.row_len and 0 <= neighbor[1] < self.col_len:
                result.append(neighbor)
        return result

    @staticmethod
    def pop_min_risk(list):
        list.sort(reverse=True, key=Node.get_total_risk)
        return list.pop()
        
    @staticmethod
    def estimate_risk(from_cell, to_cell):
        return (abs(to_cell[0] - from_cell[0]) + abs(to_cell[1] - from_cell[1]))
        
    def get_risk(self, cell):
        grid_row = cell[0] % self.row_len
        grid_col = cell[1] % self.col_len
        row_offset = cell[0] // self.row_len
        col_offset = cell[1] // self.col_len
        return ((self.grid[grid_row][grid_col] + row_offset + col_offset - 1) % 9) + 1

    def use_a_star_to_find_path(self, start, end):
        self.nodes[start].status = Node.open    
        open_list = [self.nodes[start]]
        
        while len(open_list) > 0:
            node = Map.pop_min_risk(open_list)
            self.nodes[node.cell].status = Node.closed
            print(node.cell)
            if node.cell == end:
                return self.nodes[node.cell].risk
                
            neighbors = self.get_neighbors(node.cell)
            for neighbor_cell in neighbors:
                neighbor_cell = tuple(neighbor_cell)
                neighbor_node = self.nodes[neighbor_cell]
                if neighbor_node.status == Node.closed:
                    continue
                    
                neighbor_risk = self.get_risk(neighbor_cell)
                risk = node.risk + neighbor_risk
                if neighbor_node.status != Node.open:
                    risk_to_end = Map.estimate_risk(neighbor_cell, end)
                    neighbor_node.risk = risk
                    neighbor_node.est_remaining_risk = risk_to_end
                    neighbor_node.previous = node
                    neighbor_node.status = Node.open
                    self.nodes[neighbor_cell] = neighbor_node
                    open_list.append(neighbor_node)
                elif risk < neighbor_node.risk:
                    neighbor_node.risk = risk
                    neighbor_node.previous = node
                    self.nodes[neighbor_cell] = neighbor_node
        return None

@dataclass
class Node:
    unknown = -1
    closed = 0
    open = 1

    cell: Tuple 
    previous: Tuple
    risk: int
    status: int = unknown

    def __post_init__(self):
        self.est_remaining_risk:int = self.risk

    def get_total_risk(self):
        return self.risk + self.est_remaining_risk
        
    def __repr__(self):
        return f"{self.cell} {self.risk} {self.get_total_risk()}"


def main() -> None:
    with open("input.txt", "r") as input_file:
        position_matrix = [list(_) for _ in [_.strip() for _ in input_file]]
    for line in position_matrix:
        for index, number in enumerate(line):
            line[index] = int(number)
    map = Map(position_matrix)
    print(map.use_a_star_to_find_path((0,0), 
    (len(position_matrix[0]) -1, len(position_matrix) -1)
    ))

if __name__ == '__main__':
    main()