import numpy as np
import pickle
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


def comparison(part, template_name, input_name):

  score = 0

  filename = "g_nums" + str(part) + ".txt"
  name = os.path.join("./output_data/", filename)
  print(filename)
  with open(name, 'rb') as fp:
    distance = pickle.load(fp)
  
  for i in range(100):
    match = np.min(distance[i])
    match_index = np.argmin(distance[i])
    #print("dist = ", match)

    match_word = input_name[match_index]
    #print("template = ", template_name[0])
    #print("match word = ", match_word)
    if template_name[i] == match_word:
      score+=1
    
    elif template_name[i] != match_word:
      print(i)
      print("template = ", template_name[i])
      print("match word = ", match_word)
  
  score = score/100
  
  print("accuracy = ", score)

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

  for i in range(4):
    number = "0" + str(i)
    print("------------ start " + number + " ----------------")
    comparison(number, word[0], word[i])


if __name__ == "__main__":

  main()
