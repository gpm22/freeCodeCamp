import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **names):
    self.names = names
    self.contents = []
    chaves = list(self.names.keys())
    for i in range(len(self.names)):

      self.contents.extend([chaves[i]]*self.names[chaves[i]])

  def draw(self, num_balls):
    teste = self.contents[:]
    retiradas = []
    if num_balls >= len(self.contents):

      self.contents = []
      return teste

    for _ in range(num_balls):
      a = random.choice(self.contents)
    

      retiradas.append(a)
      self.contents.remove(a)

    return retiradas


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  M = 0
  esperadas = []
  chaves = list(expected_balls.keys())

  for i in range(len(expected_balls)):
    esperadas.extend([chaves[i]]*expected_balls[chaves[i]])

  for _ in range(num_experiments):
    hat_1 = copy.deepcopy(hat)
    bolas_retiradas = hat_1.draw(num_balls_drawn)

    a = 0
    for espero in esperadas:

      if espero in bolas_retiradas: 
        a+=1
        bolas_retiradas.remove(espero)


    if a == len(esperadas): M+=1

  return M/num_experiments
