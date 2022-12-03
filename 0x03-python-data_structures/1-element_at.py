#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
    if idx < 0 or idx > len(my_list):
        print("None")
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
