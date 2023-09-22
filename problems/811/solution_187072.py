# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao_porta(lista,H,L):
    '''verifica se o colchao de medidas [a,b,c] passa pela porta de medidas H e L
    a<b<c
    H = altura
    L = largura
    list, int, int -> bool'''
    [a,b,c]=lista
    if a>H or a>L or b>H:
        return False
    else:
        return True