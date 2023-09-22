# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''pega a palavra s e substitui a letra i pelo
    caractere x'''
    j = i + 1
    tamanho = len(s)
    palavra = s[0:i] + x + s[j:tamanho]
    return palavra