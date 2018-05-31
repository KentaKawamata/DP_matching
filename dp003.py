import numpy as np
import os

def main():

  filename = "city011_001.txt"
  dirname = "./datasets/city011/"
  name = os.path.join(dirname, filename)

  with open(name, "r") as fp:
    city = fp.readlines()


  
  datas = []
  for i, line in enumerate(city):
    if i==0:
      sireal = str(line)
      sireal = sireal.replace('\n', '')
    if i==1:
      city_name = str(line)
      city_name = city_name.replace('\n', '')
    if i==2:
      file_num = int(line)
    else:
      datas.append(line)

  data=" "
  for i in datas:
    data += i

  data = data.replace('\n', '')
  print(sireal)
  print(city_name)
  print(file_num)
  print(data)

if __name__ == "__main__":

  main()
