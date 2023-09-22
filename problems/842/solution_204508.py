def pontos_por_time(l):
  '''Função que recebe uma lista l com nomes de dois times e resultados de jogos entre eles e retorna o número de pontos que cada time fez nesses jogos entrada:list, saída:dict'''
if l[3][1]==l[3][2] and l[6][1]==l[6][2]:
    print {'l[1]':2, 'l[2]':2}
elif l[3][1]>l[3][2] and l[6][1]>l[6][2]:
    print {'l[1]':3, 'l[2]':3}
elif l[3][1]>l[3][2] and l[6][1]<l[6][2]:
    print {'l[1]':6, 'l[2]':0}
elif l[3][1]<l[3][2] and l[6][1]>l[6][2]:
    print {'l[1]':0, 'l[2]':6}
elif l[3][1]>l[3][2] and l[6][1]==l[6][2]:
    print {'l[1]':4, 'l[2]':1}
elif l[3][1]<l[3][2] and l[6][1]==l[6][2]:
    print {'l[1]':1, 'l[2]':4}
elif l[3][1]==l[3][2] and l[6][1]<l[6][2]:
    print {'l[1]':4, 'l[2]':1}
elif l[3][1]==l[3][2] and l[6][1]>l[6][2]:
    print {'l[1]':1, 'l[2]':4}