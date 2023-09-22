# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma palavra, uma string e um número inteiro
    	e substitui na palavra a string na posição i
        ex: ('parabens','u',1) = ('purabens')'''
    LS = i-len(s)
    LI = i-len(s)+1
    Str = s[:LS]+str(x)+s[LI:]
    return Str