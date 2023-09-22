# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função substitui a letra da posição i pelo caractere x'''
    inicio = s[0:i]
    final = s[i:]
    return inicio+str(x)+final