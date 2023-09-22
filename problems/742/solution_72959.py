# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
  string_lista = [s[0:i], s[i:]
  string = string_lista[0] + x + s[1]
  return string