# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string s, trocando o elemento de posição i dessa string por um caractere x.'''
    posicao=s[i]
    palavra_nova= s.replace(posicao,x,1)
    return palavra_nova