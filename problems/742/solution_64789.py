# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Calcula e retorna uma string s, mas trocando o elemento de 
    posição i pelo caractere x'''
    '''str,str,int->str'''
    q=len(s)
    '''q é a quantidade de caracteres em s'''
    y=i+1
    '''y vai servir como o caractere após o de cordenada i'''
    return s[0:i]+str(x)+s[y:q]