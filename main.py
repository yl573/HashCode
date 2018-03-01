
class ride:
    def __init__(self, a, b, x, y, s, f, index):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.index = index

class vehicle:
    def __init__(self, x=0, y=0, end_time=0):
        self.x = x
        self.y = y
        self.end_time = end_time


def split_line(s):
    return list(map(int, s.split(' ')))

def read_data(file_name):

    with open(file_name,'r') as f:
        text = f.read()
        lines = text.split('\n')[:-1]

        R, C, F, N, B, T = split_line(lines[0])

        rides = []

        for i, line in enumerate(lines[1:]):
            ride = split_line(line)
            ride.append(i)
            # a, b, x, y, s, f
            rides.append(tuple(ride))

    return R, C, F, N, B, T, rides


def init_ride_list(rides_list):
    '''
    :param raw_data:
    :return:
    sort w.r.t. start timestamp
    //potential: sort w.r.t. dist+bonus, dist from available car
    '''
    rides_list.sort(key=lambda x: x.s)
    return rides_list


def update_vehicle_list(vehicles_list, new_vehicle):
    vehicles_list.append(vehicle)
    return vehicles_list

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def search_available_vehicle(ride, car_list):
    '''
    :param ride_list:
    :param car_list:
    :return:
    rule: (vehicle endtime - ride starttime) <= ride starttime - vehicle endtime
    currently, assign the first find
    '''
    for car_index, car in enumerate(car_list):
        if distance(ride.a, ride.b, car.x, car.y) + car.end_time < ride.s:  
            return car_index
    return None

def output(result):
    with open('output','w') as f:
        for i,res in enumerate(result):
            s = str(len(res)) + ' '
            for ride in res:
                s += str(ride) + ' '
            s += '\n'
            f.write(s)

# R, C, F, N, B, T, rides = read_data('a_example.in')
# R, C, F, N, B, T, rides = read_data('b_should_be_easy.in')
R, C, F, N, B, T, rides = read_data('d_metropolis.in')

rides_list = [ride(*r) for r in rides]
car_list = [vehicle() for i in range(F)]
result = [[] for i in range(F)]

rides_list = init_ride_list(rides_list)

for ride in rides_list:
    i = search_available_vehicle(ride, car_list)
    if i is not None:
        car = car_list[i]
        result[i].append(ride.index)
        car_list[i].x = ride.x
        car_list[i].y = ride.y
        car_list[i].end_time += distance(ride.a, ride.x, ride.b, ride.y) + distance(ride.a, ride.b, car.x, car.y)

print(result)

output(result)




