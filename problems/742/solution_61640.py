# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que retorne a string s e substitui i pelo caractere x, dada
    	as entradas. str, int --> str, int.'''
    f=s[0:i]
    f=f+str(x)
    return= f+s [i+1:]