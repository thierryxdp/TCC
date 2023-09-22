# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma nova string substituindo a string s na posição i pelo caractere x
    	str,str,int->str'''
    
    nova_str=s[0:i]+x+s[i+1:]
    return nova_str