# Tianze Ren, tr2bx, 03/20/2023
def bakeoff(input_list):
    # input: a list of pairs or floats (active time, passive time)
    # output: index of the component to make first
    largest = 0;
    for i in input_list:
        if i[1] > input_list[largest][1]:
            largest = input_list.index(i)
        if i[1] == input_list[largest][1]:
            if i[0] < input_list[largest][0]:
                largest = input_list.index(i)
    return largest

def deadlines(input_list):
    # input: a list of pairs or floats (completion time, due time)
    # output: index of the assignment to complete first
    smallest = 0;
    for i in input_list:
        if i[1] < input_list[smallest][1]:
            smallest = input_list.index(i)
        if i[1] == input_list[smallest][1]:
            if i[0] > input_list[smallest][0]:
                smallest = input_list.index(i)
    return smallest

def mileage(input_list):
    # input: a list of pairs or floats (mpg, miles)
    # output: index of the car to deliver first
    largest = 0
    for i in input_list:
        if i[1]/i[0] > input_list[largest][1]/input_list[largest][0]:
            largest = input_list.index(i)
    return largest