
class ride:
    def __init__(self, a, b, x, y, s, f, index)
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.index = index

class vehicle:
    def __init__(self, endx, endy, end_time):
        self.endx = endx
        self.endy = endy
        self.end_time = end_time


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


def init_ride_list(rides_list):
    '''
    :param raw_data:
    :return:
    sort w.r.t. start timestamp
    //potential: sort w.r.t. dist+bonus, dist from available car
    '''
    rides.sort(key=lambda x: x.s)
    return rides_list


def update_vehicle_list(vehicles_list, new_vehicle):
    vehicles_list.append(vehicle)
    return vehicles_list

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def search_available_vehicle(ride_list, car_list, result):
    '''
    :param ride_list:
    :param car_list:
    :return:
    rule: (vehicle endtime - ride starttime) <= ride starttime - vehicle endtime
    currently, assign the first find
    '''

    for ride in ride_list:
        for i, car in enumerate(car_list):
            if distance(ride.x, ride.y, car.a, car.b) + car.end_time = ride.s:
                result[i].append(ride.index)
                
                break


    return selected_car

R, C, F, N, B, T, rides = read_data('a_example.in')




