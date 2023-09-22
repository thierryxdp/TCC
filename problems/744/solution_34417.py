def hashtag(st):
  #Função que recebe uma string e insire o caractere "#" no seu início, meio e fim
  if len(st) % 2 == 0:
    #Se a quantidade de caracteres da string for par
    metadeP = len(st) / 2
    return '#' + st[0:int(metadeP)] + '#' + st[int(metadeP):] + '#'
  elif len(st) % 2 != 0:
    #Se a quantidade de caracteres da string for ímpar
    metadeI = len(st) // 2
    return '#' + st[0:int(metadeI)] + '#' + st[int(metadeI):] + '#'