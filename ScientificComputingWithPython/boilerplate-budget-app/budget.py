class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):

    self.ledger.append({'amount': amount, 'description': description})

  def withdraw(self, amount, description=''):
    #atual = sum([i['amount'] for i in self.ledger])
    #atual = get_balance(self)
    if self.check_funds(amount):
      self.ledger.append({'amount': -1*amount, 'description': description})
      return True
    else:
      return False

  def get_balance(self):
    return sum([i['amount'] for i in self.ledger])

  def transfer(self, amount, another_category):

    #atual = get_balance(self)
    if self.check_funds(amount):
      description_1 = 'Transfer to '+ another_category.name
      self.withdraw(amount, description_1)
      description_2 = 'Transfer from '+ self.name
      another_category.deposit(amount, description_2)

      return True

    else: return False

  def check_funds(self, amount):
    atual = self.get_balance()

    if amount <= atual: return True
    else: return False

  def __str__(self):

    cte = (30-len(self.name))//2
    linhas = []
    linhas.append('*'*cte + self.name + '*'*cte)
    
    for a in self.ledger:

      if a['amount']//1 == a['amount']: 
        valor = str(a['amount'])+'.00'
      else: 
        valor = str(a['amount'])

      b = 30 - len(valor)
      c = len(a['description'])
      cte =  b - c

      if c > b:
        cte = 1
        linhas.append(a['description'][:b-1] + ' '*cte + valor)
      else:
        linhas.append(a['description'] + ' '*cte + valor)

    linhas.append('Total: ' + str(self.get_balance()))

    
    imagem = '\n'.join(linhas)

    return imagem


def create_spend_chart(categories):
  linhas = []
  linhas.append('Percentage spent by category')
  gastos = []

  for categoria in categories:
    gastos.append(sum([i['amount'] for i in categoria.ledger if i['amount'] < 0]))

  #print('gastos: ',gastos, '\n')

  f = lambda x: (int((x/gasto_total)*10))*10

  gasto_total = sum(gastos)

  #print('gasto total:', gasto_total, '\n')

  porcentagem = list(map(f, gastos))

  #print('porcentagem :', porcentagem, '\n')

  largura = len(categories)

  n = 100
  c = 0
  for i in range(11):
    if len(str(n)) == 2: c=1
    if len(str(n)) == 1: c=2
    linha = ' '*c + str(n) + '|'

    for valor in porcentagem:
      if valor >= n: linha = linha + ' o '
      else: linha = linha + ' '*3


    linhas.append(linha + ' ')

    n-=10


  linhas.append(' '*4 + '-'*(largura*3+1))

  nomes = [i.name for i in categories]

  profundidade = max(list(map(len, nomes)))
  #menor = min(list(map(len, nomes)))

  for i in range(len(nomes)):

    a = len(nomes[i])
    if  a < profundidade:
      nomes[i] = nomes[i] + ' '*(profundidade-a)


  for i in range(profundidade):
    linha = '    '
    for nome in nomes:
      linha = linha + ' ' + nome[i] + ' '
    
    linhas.append(linha+ ' ')

  return '\n'.join(linhas)


#test_to_string

#test_create_spend_chart

