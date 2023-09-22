def maiores(lista_numeros,inteiro):
    'função que retorna todos os termos de uma lista maiores que n'
    list.sort(lista_numeros)
    i=inteiro
    return lista_numeros[i+1:]