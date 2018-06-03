import numpy as np
import os

def readfiles(filename, dirname):

  name = os.path.join(dirname, filename)

  with open(name, "r") as fp:
    city = fp.readlines()

  datas = []
  for i, line in enumerate(city):
    if i==0:
      sireal = str(line)
      sireal = sireal.replace('\n', '')
    elif i==1:
      city_name = str(line)
      city_name = city_name.replace('\n', '')
    elif i==2:
      continue
    else:
      line = line.replace('\n', '')
      line = line.split()
      datas.append(line)

  data = np.array(datas, dtype=float)

  return sireal, city_name, data.shape[0], data

def  caluclate_local_distance(template_num, input_num, template_data, input_data):

  print("----- start caluclate distane-----")
  word_num = 100
  matrix_list = [[] for j in range(word_num)]

  for temp_number in range(word_num):
    print("----- Next words caluclate -----")
    for m in range(word_num):
      matrix = np.zeros((input_num[m], template_num[temp_number]))

      for y in range(input_num[m]):
        for x in range(template_num[temp_number]):
          matrix[y,x] = np.sum((template_data[temp_number][x,0:14] - input_data[m][y,0:14])**2)
  
      matrix = np.sqrt(matrix)
      matrix_list[temp_number].append(matrix)

  #print(matrix)
  return matrix_list

def dp_matching(template_num, input_num, matrixs):
  
  print("----- Start DP matching -----")
  word_num = 100
  g_list = [[] for n in range(word_num)]
  g_nums = [[] for n in range(word_num)]

  for n in range(word_num):
    for m in range(word_num):

      d = matrixs[n][m]
      g = np.zeros((input_num[m],template_num[n]))
      g[0,0] = d[0,0]

      for j in range(1, input_num[m]):
        g[j,0] = g[j-1,0] + d[j,0]
      for i in range(1, template_num[n]):
        g[0,i] = g[0,i-1] + d[0,i]

      for y in range(1, input_num[m]):
        for x in range(1, template_num[n]):
          number = np.array([10000]*3)

          if y < input_num[m]:
            number[0] = g[y,x-1] + d[y,x]
          if x<template_num[n] and input_num[m]:
            number[1] = g[y-1,x-1] + d[y,x]
          if x < template_num[n]:
            number[2] = g[y-1,x] + d[y,x]
    
          number_min = number.min() 

          g[y,x] = number_min
          
      g_num = g[-1,-1]
      g_num = g_num / (template_num[n] + input_num[m])
      print("gnums = ", g_nums)
      g_list[n].append(g)
      g_nums[n].append(g_num)

  return g_list, g_nums

def comparison(template_name, input_name, dis):

  print("template = ", template_name[0])
  
  match = np.min(dis[0])
  match_index = np.argmin(dis[0])
  print("dist = ", match)

  match_word = input_name[match_index]
  print("match word = ", match_word)
  
def main():  

  name = [[] for j in range(4)]
  word = [[] for j in range(4)]
  num = [[] for j in range(4)]
  data = [[] for j in range(4)]
  for j in range(4):
    if j<2:
      human=1
    elif j>=2:
      human=2
    if j%2==0:
      number=1
    elif j%2!=0:
      number=2
    
    dirname = "./datasets/city0" + str(human) + str(number) + "/"
    for i in range(100):
      filename = "city0" + str(human) + str(number) + "_" + str("{0:03d}".format(i+1)) + ".txt"

      sireal, word1, num1, data1 = readfiles(filename, dirname)
      name[j].append(sireal)
      word[j].append(word1)
      num[j].append(num1)
      data[j].append(data1)
  
  matrix_1 = caluclate_local_distance(num[0], num[1], data[0], data[1])
  #matrix_2 = caluclate_local_distance(num[0], num[2], data[0], data[2])
  #matrix_3 = caluclate_local_distance(num[0], num[3], data[0], data[3])

  matching1, distance_1 = dp_matching(num[0], num[1], matrix_1)

  comparison(word[0], word[1], distance_1)

  print("dis1 = ", dis1)

if __name__ == "__main__":

  main()
