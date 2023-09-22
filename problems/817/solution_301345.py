def maiores(lista_numero,n):
    """
    Função que dados, respectivamente, uma lista ordenada(crescente)
    de numeros inteiros, e um número inteiro, retorna uma lista somente com
    os numeros maiores que n
    list , int ---> list
    """
    list.sort(lista_numero)
    indice=(list.index(lista_numero,n))+1
    return l1[indice:]

def acima_da_media(notas):
    """
    Função que dados uma lista de notas, e ua média, retorna
    uma lista ordenada com todas as notas acima da média
    """
    m=sum(notas)
    l=len(notas)
    media=m/l
    return maiores(notas,media)