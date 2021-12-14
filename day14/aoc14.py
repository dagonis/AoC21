from collections import Counter

def main() -> None:
    with open('input.txt', 'r') as input_file:
        lines = [_.strip() for _ in input_file]
    template = lines[0]
    pairs = {}
    for line in lines[2:]:
        k, v = line.split(' -> ')
        pairs[k] = v
    ### Part 1
    # Leaving this for Posterity, this solution was fine until the numbers
    # involved got real big. I actually though updating the string and keeping track
    # of where the insertions were was a decent idea. It did get my the right answer for
    # part 1!
    ###
    # for n in range(10):
    #     print(n)
    #     template = "".join([_ for _ in template])
    #     insertions = set()
    #     replacement_index = 0 
    #     for pair in pairs.keys():
    #         index = 0
    #         while index < len(template):
    #             location = template.find(pair, index)
    #             if not location == -1:
    #                 insertions.add((location, pair))
    #             index += 1
    #     insertions = list(insertions)
    #     insertions.sort()
    #     for insertion in insertions:
    #         i, pair = insertion
    #         template = list(template)
    #         template.insert(i+replacement_index+1, pairs[pair])
    #         replacement_index += 1
    # counts = Counter(template)
    # print(counts.most_common()[0][1] - counts.most_common()[-1][1])
    ### Part 2
    poly_counter = Counter()
    for i in range(len(template)-1):
        poly_counter[template[i:i+2]] += 1
    for _ in range(40):
        update_counter = Counter()
        for k in poly_counter:
            left, right = f'{k[0]}{pairs[k]}', f'{pairs[k]}{k[1]}'
            update_counter[left] += poly_counter[k]
            update_counter[right] += poly_counter[k]
        poly_counter = update_counter
    molecule_counts = Counter()
    for k in poly_counter:
        molecule_counts[k[0]] += poly_counter[k]
    molecule_counts[template[-1]] += 1 #This is for the dangling last molecule from the original input, otherwise one of the molecules is off by one
    print(molecule_counts.most_common()[0][1] - molecule_counts.most_common()[-1][1]) 


if __name__ == '__main__':
    main()