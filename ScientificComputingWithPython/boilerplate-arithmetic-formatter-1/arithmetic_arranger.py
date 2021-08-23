def arithmetic_arranger(problems,solution = False):

  if len(problems) > 5 :
    return 'Error: Too many problems.'

  arranged_problems = []
  linha_1 = []
  linha_2 = []
  linha_3 = []
  linha_4 = []

  for problema in problems:
    componentes = problema.split()

    if componentes[1] != '+' and componentes[1] != '-':
      return "Error: Operator must be '+' or '-'."
      

    if componentes[0].isdecimal() == False or componentes[2].isdecimal() == False:
      return "Error: Numbers must only contain digits."
    
    maior = 0

    tma_1 = len(componentes[0])
    tma_2 = len(componentes[2])

    if tma_1 > 4 or tma_2 > 4:
      return "Error: Numbers cannot be more than four digits."
    
    if tma_1 >= tma_2:
      maior = tma_1
      cte_1 = 2
      cte_2 = tma_1 - tma_2 + 1
    else:
      maior = tma_2
      cte_1 = tma_2 - tma_1 + 2
      cte_2 = 1
    
    cte_3 = maior+2

    linha_1.append(' '*cte_1 + componentes[0])
    linha_2.append(componentes[1] + ' '*cte_2 + componentes[2])
    linha_3.append('-'*cte_3)

    if solution:

      if componentes[1] == '+':
        resultado = int(componentes[0]) + int(componentes[2])
      else:
        resultado = int(componentes[0]) - int(componentes[2])

      resultado = str(resultado)

      cte_4 = cte_3 - len(resultado)

      linha_4.append(' '*cte_4 + resultado)

  linha_1 = '    '.join(linha_1)
  linha_2 = '    '.join(linha_2)
  linha_3 = '    '.join(linha_3)

  arranged_problems = linha_1 + '\n' + linha_2 + '\n' + linha_3

  if solution:
    linha_4 = '    '.join(linha_4)
    arranged_problems = arranged_problems + '\n' + linha_4


  return arranged_problems