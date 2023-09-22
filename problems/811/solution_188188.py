def colchao(medidas,H,L):
    '''função que recebe como entrada a lista "medidas", com as 3 dimensões
do colchão(um paralelepípedo reto) listadas do menor tamanho ao maior em
centímetros; e recebe a altura H e a largura L da porta, medidas em centímetros;
retornando "True" se o colchão pode passar pela porta e "False" se não passar;
list,int,int->bool'''

    [A,B,C]=medidas
    m=min(H,L)
    M=max(H,L)

    if A<=m and B<=M:
        return True

    else:
        return False