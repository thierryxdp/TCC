# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' funcao que calcula a soma dos 3 e retorna somente s quando 
   i troca de lugar com x
   s-> str; x-> caractere; i-> int'''
  
 return s[0:i]+x+s[i+1: ]