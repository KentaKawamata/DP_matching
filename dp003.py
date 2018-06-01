import numpy as np
import os

def readfiles(filename, dirname):

  name = os.path.join(dirname, filename)
  #print(name)

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
  #print(sireal)
  #print(city_name)
  #print(data.shape)
  ##print(data)

  return sireal, city_name, data.shape[0], data

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
      #print(sireal)
      name[j].append(sireal)
      word[j].append(word1)
      num[j].append(num1)
      data[j].append(data1)
    
  matrix = np.zeros((num[1][0], num[0][0]))
        

  print(name[0][0])
  print(name[3][0])
  print(data[0][0][0,0:14])
  print(data[3][0][0,0:14])
  
  for y in range(num[1][0]):
    for x in range(num[0][0]):
      matrix[y,x] = np.sum((data[0][0][x,0:14]-data[1][0][y,0:14])**2)
  
  matrix = np.sqrt(matrix)
  print(matrix)

if __name__ == "__main__":

  main()
