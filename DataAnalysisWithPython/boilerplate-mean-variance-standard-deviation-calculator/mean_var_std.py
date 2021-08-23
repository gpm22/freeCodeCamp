import numpy as np

def calculate(list_1):

  if len(list_1) < 9:
    raise ValueError('List must contain nine numbers.')

  calculations = {}

  array_1 = np.array(list_1)

  matrix_1 = np.reshape(array_1,(3, 3))

  names = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']

  functions = [lambda x: x.mean(), lambda x: x.var(), lambda x: x.std(), lambda x: x.max(), lambda x: x.min(), lambda x: x.sum()]

  for i in range(6):

    calculations[names[i]] = [[],[],[]]

    #axis1 (column) calculations
    for j in range(3):
      calculations[names[i]][0].append(functions[i](matrix_1[:,j]))

    #axis2 (rows) calculations
    for j in range(3):
      calculations[names[i]][1].append(functions[i](matrix_1[j]))

    #flattened calculations
    calculations[names[i]][2] = functions[i](array_1)

    #print(i)
    #print(names[i])
    #print(functions[i])

    

  return calculations