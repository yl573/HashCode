
class ride:
    def __init__(self, a, b, x, y, s, f)
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f

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

def init_ride_list(raw_data):
    '''
    :param raw_data:
    :return:
    sort w.r.t. start timestamp
    //potential: sort w.r.t. dist+bonus, dist from available car
    '''
    return ride_list

def update_vehicle_list():
    pass


def search_available_vehicle(ride_list, car_list):
    '''
    :param ride_list:
    :param car_list:
    :return:
    rule: (vehicle endtime - ride starttime) <= ride starttime - vehicle endtime
    currently, assign the first find
    '''
    for ride in ride_list:
        for car in car_list:
            if abs(car.endx - ride.x) + abs(car.y - ride.y) + car.end_time = ride.start_time

    return selected_car

R, C, F, N, B, T, rides = read_data('a_example.in')




