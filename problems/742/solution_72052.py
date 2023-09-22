# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
  '''Função que recebe a string 's', o caractere 'x' e um valor 'i', e gera uma nova string 's1'
  que substitui o caractere correspondente ao valor 'i' na string 's'.
  str -> str'''
  s1 = s[:i] + x + s[i+1:]
  return s1