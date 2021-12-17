def main() -> None:
    with open('input.txt', 'r') as input_file:
        raw_test_area = [_.rstrip() for _ in input_file][0].lstrip('target area: ')
    x, y = raw_test_area.split(', ')
    x1, x2 = [int(_) for _ in x.lstrip('x=').split('..')]
    y1, y2 = [int(_) for _ in y.lstrip('y=').split('..')]
    safe_zone =  [[x, y] for x in range(x1, x2+1) for y in range(y1, y2+1)]
    velocities = [[x, y] for x in range(0, x2+1) for y in range(-200, 200)]
    max_ys = []
    for velocity in velocities:
        current_position = [0,0]
        max_y = 0
        while not (current_position in safe_zone) and not (current_position[0] > x2+1 or current_position[1] < y1):
            max_y = current_position[1] if current_position[1] > max_y else max_y
            current_position[0] += velocity[0]
            current_position[1] += velocity[1]
            if velocity[0] > 0:
                velocity[0] -= 1
            elif velocity[0] < 0:
                velocity[0] += 1
            velocity[1] -= 1
        else:
            if current_position in safe_zone:
                max_ys.append(max_y)
    print(max(max_ys))
    print(len(max_ys))

if __name__ == '__main__':
    main()