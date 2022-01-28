def more_vowels(foo):

  arr = list(foo)
  vowel = 0
  const = 0

  for a in arr:
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
      vowel += 1 
    else:
      const += 1
  
  if (vowel > const):
    return True
  elif (const > vowel):
    return False
  else:
    return None

import math

def volume(R,H):
  volume = math.pi * R * R * H
  return volume

# volume = volume(3,3)
# print(volume)

def csv(list):
  string = ",".join(list)
  return string

# list = ["a","b","c","d","e"]
# string = csv(list)
# print(string)

def write_to_file(list):
  f = open("file.txt", "a")
  for list in list:
    f.write(csv(list))
  f.close()

def red_file(filename):
  final_list = []
  with open(filename, 'rb') as csvfile:
    for row in csvfile:
      final_list.append(row)
  return final_list
      

def try_except(a, b):
  try:
    c = a / b
    return c
  except ZeroDivisionError:
    print ("zero denominator")


def no_duplicates(list):
  final = []
  for l in list:
    if l not in final:
      final.append(l)
      #print(l)
  return final

# list = [1,1,1,2,2,3,4,5,4,6,2,3,4,5,8]
# a = no_duplicates(list)
# print(a)

import os

def make_dir():
  directory = "“hw3-folder"
  parent = os.getcwd()
  path = os.path.join(parent, directory) 
  os.mkdir(path)