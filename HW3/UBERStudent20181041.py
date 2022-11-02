#!/usr/bin/python3

import sys
import calendar

input_file = sys.argv[1]
output_file = sys.argv[2]
weekday_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
uber_dict = dict()

with open(input_file, "rt") as fp:
	for line in fp:
		uber = line.split(",")
		dayList = uber[1].split("/")
		day = calendar.weekday(int(dayList[2]), int(dayList[0]), int(dayList[1]))
		n = uber[0]
		vehicle = int(uber[2])
		trip = int(uber[3][:-1])
		key = n + "," + weekday_list[day]

		if key in uber_dict:
			value = uber_dict[key].split(",")
			vehicle += int(value[0])
			trip += int(value[1])
		uber_dict[key] = str(vehicle) + "," + str(trip)

with open(output_file, "wt") as fp:
	items = uber_dict.items()
	for item in items:
		fp.write(item[0] + " " + str(item[1]) + "\n")
