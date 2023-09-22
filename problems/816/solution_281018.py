def maiores(lista_numeros,inteiro):
    'função que retorna todos os termos de uma lista maiores que n'
    lista_numeros=lista_numeros+[inteiro]
    list.sort(lista_numeros)
    posicao_inteiro=list.index(lista_numeros,inteiro)
    return lista_numeros[posicao_inteiro+1:]