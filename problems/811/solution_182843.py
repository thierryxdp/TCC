# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Função que avalia se o colchão, de medidas A, B e C, que serão
    dispostos na entrada em forma de lista(e em ordem crescente), passará
    pelas portas da residência, as quais possuem dimensões H e L,
    correspondentes a altura e largura
    	list[int,int,int],int,int -> bool
    '''
    a,b,c = medidas
    if (c<=H and b<=L) or (c<=L and b<=H) or (b<=H and a<=L) or (a<=H and b<=L):
        answer = True
    else:
        answer = False
    return answer