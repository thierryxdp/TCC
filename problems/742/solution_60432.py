# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
'''Função que receba um recebe uma string, um caractere e um inteiro e substitui e retorne uma string com com o elemento i substituído por x
str,str,int -> str'''
   return s[0:i]+x+s[i+1:len(s)]