# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
  '''função que retorna uma string igual a (s),
  uma caractere x e um número inteiro (i) entre 0 e o
  comprimento da string, exceto que o elemento
  da posição (i) deve ser substituido pelo caractere x;
  str,int,int,int -> string'''
  return s[0:i] + x+ s[i+1:len(s)]