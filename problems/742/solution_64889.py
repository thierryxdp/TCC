# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Funcão que recebe uma string "s", um caractere "x"
    e um número inteiro "i" entre 0 e o comprimento da string
    "s" e substitui o elemento da posição "i" pelo caractere "x"'''
    '''str, str, int -> str'''
    #Casos de teste:
    '''substitui('Felipe','t',5)-> Felipt
       substitui('informática','b',7)->informábica
       substitui('química','x',1)->qxímica'''
    return s[0:i] + str(x) + s[i+1:len(s)]