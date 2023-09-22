# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' funçao que soma s,x,i 
    e retorna somente s quando i trocaa de lugar com o x''' 
  
   return s[0:i]+x+s[i+1: ]