import numpy as np

def main():

  d = np.array([[1, 2, 2, 2, 1, 3],
                [1, 3, 1, 3, 2, 2],
                [3, 2, 2, 1, 3, 2],
                [1, 1, 3, 1, 3, 3],
                [2, 3, 1, 1, 2, 2]])

  g = np.zeros((5,6))
  bunki = np.zeros((5,6))
  route = np.zeros((5,6))
  g[0,0]= d[0,0]
  
  bunki[0,:] = 1
  bunki[:,0] = 3

  for j in range(1,5):
    g[j,0] = g[j-1,0] + d[j,0]
  for i in range(1,6):
    g[0,i] = g[0,i-1] + d[0,i]

  for y in range(1,5):
    for x in range(1,6):
      number = np.array([1000]*3)
     
      if y<5:
        number[0] = g[y,x-1] + d[y,x]
      if x<6 and y<5:
        number[1] = g[y-1,x-1] + 2*d[y,x]
      if x<6:
        number[2] = g[y-1,x] + d[y,x]

      num_min = number.min()
      
      if num_min == number[0]:
        bunki[y,x] = 1
      if num_min == number[1]:
        bunki[y,x] = 2
      if num_min == number[2]:
        bunki[y,x] = 3
      
      g[y,x] = num_min

  y, x = 4, 5
  route[y,x] = 1
  while True:
    if bunki[y,x] == 1:
      route[y,x-1] = 1
      x-=1
    if bunki[y,x] == 2:
      route[y-1,x-1] = 1
      x-=1
      y-=1
    if bunki[y,x] == 3:
      route[y-1,x] = 1
      y-=1
    if x<=0 and y<=0:
      break


  print(g)
  print(route)
  print(bunki)

if __name__ == "__main__":

  main()
