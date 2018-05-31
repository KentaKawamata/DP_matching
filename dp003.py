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
  data = np.reshape(data, (data.size))
  print(sireal)
  print(city_name)
  print(data.shape)
  print(data)

  return sireal, city_name, data.size, data

def main():  

  sireal1, word1, num1, data1 = readfiles("city011_001.txt", "./datasets/city011/")
  sireal2, word2, num2, data2 = readfiles("city012_001.txt", "./datasets/city012/")

  matrix = np.zeros((num2, num1))
  
  print(data1.shape)

  for y in range(num2):
    for x in range(num1):
      matrix[y,x] = data2[y] - data1[x]
  
  print(matrix)

if __name__ == "__main__":

  main()
