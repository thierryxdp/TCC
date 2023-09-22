def hashtag(st):
  #Função que recebe uma string e insire o caractere "#" no início, meio e fim
  if len(st) % 2 == 0:
    #Se a quantidade de caracteres da string for par
    return '#' + st[0:2] + '#' + st[2:4] + '#'
  elif len(st) % 2 != 0:
    #Se a quantidade de caracteres da string for ímpar
    return '#' + st[0:2] + '#' + st[2:5] + '#'