from typing import List

def flood_fill(basin: set, row: int, col: int,  heights: List):
    col_len, row_len = len(heights[0]), len(heights)
    if row < 0:
        return set()
    if row > row_len - 1:
        return set()
    if col < 0:
        return set()
    if col > col_len - 1:
        return set()
    if (row, col) in basin:
        return set()
    if int(heights[row][col]) == 9:
        return set()
    basin.add((row, col))
    for r, c in flood_fill(basin, row, col - 1, heights):
        basin.add((r, c))
    for r, c in flood_fill(basin, row + 1, col, heights):
        basin.add((r, c))
    for r, c in flood_fill(basin, row - 1, col, heights):
        basin.add((r, c))
    for r, c in flood_fill(basin, row, col + 1, heights):
        basin.add((r, c))
    return basin

    

def main() -> None:
    with open("input.txt") as input_file:
        heights = [_.strip() for _ in input_file]
    lowest_points = []
    for ri, row in enumerate(heights):
        for ci, col in enumerate(row):
            if (ri == 0 or ri == len(heights) - 1) and (ci == 0 or ci == len(row) - 1): # Corners
                if ri == 0 and ci == 0:
                    if col < heights[ri+1][ci] and col < heights[ri][ci+1]:
                        lowest_points.append((int(col), ri, ci))
                elif ri == 0 and ci == ci == len(row) - 1:
                    if col < heights[ri+1][ci] and col < heights[ri][ci-1]:
                        lowest_points.append((int(col), ri, ci))
                elif ri == len(heights) - 1 and ci == 0:
                    if col < heights[ri-1][ci] and col < heights[ri][ci+1]:
                        lowest_points.append((int(col), ri, ci))
                elif ri == len(heights) - 1 and len(row) - 1:
                    if col < heights[ri-1][ci] and col < heights[ri][ci-1]:
                        lowest_points.append((int(col), ri, ci))
            elif ri == 0 or ri == len(heights) - 1: # Top and Bottom Row
                if ri == 0:
                    if col < heights[ri+1][ci] and col < heights[ri][ci+1] and col < heights[ri][ci-1]:
                        lowest_points.append((int(col), ri, ci))
                elif ri == len(heights) - 1:
                    if col < heights[ri-1][ci] and col < heights[ri][ci+1] and col < heights[ri][ci-1]:
                        lowest_points.append((int(col), ri, ci))
            elif ci == 0 or ci == len(row) - 1: # Edges
                if ci == 0:
                    if col < heights[ri-1][ci] and col < heights[ri+1][ci] and col < heights[ri][ci+1]:
                        lowest_points.append((int(col), ri, ci))
                elif ci == len(row) - 1:
                    if col < heights[ri-1][ci] and col < heights[ri+1][ci] and col < heights[ri][ci-1]:
                        lowest_points.append((int(col), ri, ci))
            elif col < heights[ri-1][ci] and col < heights[ri+1][ci] and col < heights[ri][ci-1] and col < heights[ri][ci+1]:
                lowest_points.append((int(col), ri, ci))
            else:
                pass
    print(sum([_[0]+1 for _ in lowest_points]))
    basins = []
    for point in lowest_points:
        basins.append(flood_fill(set(), point[1], point[2], heights))
    basin_lens = [len(_) for _ in basins]
    basin_lens.sort()
    longest = basin_lens[-3:]
    print(longest[0] * longest[1] * longest[2])


if __name__ == '__main__':
    main()