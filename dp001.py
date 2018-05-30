#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import sys, os

def dp():

  start = 1

  d = np.array([[1, 2, 2, 2, 1, 3],
                [1, 3, 1, 3, 2, 2],
                [3, 2, 2, 1, 3, 2],
                [1, 1, 3, 1, 3, 3],
                [2, 3, 1, 1, 2, 2]])

  g = np.zeros((5,6))
  g[0,0]= d[0,0]

  number_min = 0
  dp_sum = d[0,0]
  x, y = 0, 0
  while True:
    x_sum = d.sum([j,i:5])
    y_sum = d.sum([j:4,i])
    print(x, y)
    number = np.array([[1000, 1000],[1000, 1000]])
    if x>0:
      number[0,1] = g[y,x-1] + d[y,x]
    if y>0:
      number[1,0] = g[y-1,x] + d[y,x]
    if x>0 and y>0:
      number[0,0] = g[y-1,x-1] + 2*d[y,x]
    if x==0 and y==0:
      x+=1
      y+=1
      continue

    print(number)
    number_min = number.min()
    dp_sum += number_min
    print("sum = ", dp_sum)

    #g[y,x] = number_min
    if number_min == number[0,1] and x<=5:
      x+=1
    if number_min == number[1,0] and y<=4:
      y+=1
    else:
      x+=1
      y+=1

    if x>=5:
      x=5
    if y>=4:
      y=4
    print(x, y)
    
    g[y,x] = number_min
    if x>=5 and y>=4:
      break

  print(g)
  print("dp = ", dp_sum)

  """
  for j in range(5):
    for i in range(6):
      if i==4 and j==5:
        continue
      g1 = 100
      g2 = 101
      g3 = 102
     
      if j>0:
        g1 = g[j-1,i] + d[j,i]
      elif i>0:
        g3 = g[j,i-1] + d[j,i]
      elif i>0 and j>0:
        g2 = g[j-1,i-1] + 2*d[j,i]
      if j>=0 and i>0:
        g3 = g[j,i-1] + d[j,i]
      if i>=0 and j>0:
        g1 = g[j-1,i] + d[j,i]
      if i>0 and j>0:
        g2 = g[j-1,i-1] + 2*d[j,i]
     
      if i<5 and j<=4:
        g3 = g[j,i] + d[j,i+1]
      if i<=5 and j<4:
        g1 = g[j,i] + d[j+1,i]
      if i<5 and j<4:
        g2 = g[j,i] + 2*d[j+1,i+1]

        g[j,i] = min(g1, g2, g3)
        #g[j,i] = min(g_mid, g3)
        print(g[j,i])
        number= number + g[j,i]
        if g1 > g3:
          i=5
  print(g[4,5])
  print(g)
  print(number)
  """
def main():

  dp()

if __name__ == "__main__":

  main()
