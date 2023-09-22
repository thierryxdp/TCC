# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
  '''Função que substitui o elemento na posição i da string s pelo caractere x; string,caracte,
  int-->string'''

  quant_str=len(s) 
  inteiro= i>=0 and i<=quant_str
  string_1= s[:i]+x
  mudar= i+1
  string_2= s[mudar:]
 
 
  return string_1+string_2