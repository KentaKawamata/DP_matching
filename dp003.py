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
  print(sireal)
  print(city_name)
  print(data.shape)
  #print(data)

  return sireal, city_name, data.shape[0], data

def main():  

  sireal1, word1, num1, data1 = readfiles("city011_001.txt", "./datasets/city011/")
  sireal2, word2, num2, data2 = readfiles("city012_001.txt", "./datasets/city012/")

  matrix = np.zeros((num2, num1))
  
  #for y in range(num2):
  #  for x in range(num1):

  for k in range(15):
    matrix[num2-1,num1-1] += (data1[num1-1,k]-data2[num2-1,k])**2
  
  matrix = np.sqrt(matrix)
  print(matrix)

if __name__ == "__main__":

  main()
