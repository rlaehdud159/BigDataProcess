#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

genre_dict = dict()

with open(input_file, "rt") as fp:

  for line in fp:
    movie = line.split("::")
    genre_list = movie[2].strip().split("|")

      for genre in genre_list:
        if genre not in genre_dict:
          genre_dict[genre] = 1

	else:
	  genre_dict[genre] += 1

with open(output_file, "wt") as fp:
  items = genre_dict.items()
    for item in items:
      fp.write(item[0] + " " + str(item[1]) + "\n")
