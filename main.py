def split_line(s):
    return list(map(int, s.split(' ')))

def read_data(file_name):

    with open(file_name,'r') as f:
        text = f.read()
        lines = text.split('\n')[:-1]

        R, C, F, N, B, T = split_line(lines[0])

        rides = []

        for line in lines[1:]:
            ride = split_line(line)
            # a, b, x, y, s, f
            rides.append(tuple(ride))

    return R, C, F, N, B, T, rides

R, C, F, N, B, T, rides = read_data('a_example.in')




