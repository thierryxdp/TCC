def maiores(lista_numero,n):
    """
    Função que dados, respectivamente, uma lista ordenada(crescente)
    de numeros inteiros, e um número inteiro, retorna uma lista somente com
    os numeros maiores que n
    list , int ---> list
    """
    l1=lista_numero+[n]
    list.sort(l1)
    indice=(list.index(l1,n))+1
    return l1[indice:]

def acima_da_media(notas):
    """
    Função que dados uma lista de notas, e ua média, retorna
    uma lista ordenada com todas as notas acima da média
    """
    m=sum(notas)
    l=len(notas)
    media=m/l
    lf=maiores(notas,media)
    if 6.0 in lf
    list.clear(lf)
    return lf