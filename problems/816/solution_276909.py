def maiores(lista_num,n):
    """Função que calcula uma lista dada e um numero de entrada coloca adiciona o número a lista e após isso poe em ordem crescente assim descartando numeors menores ou iguais ao nuemro dado retornando uma lista somente com os numeros maiores
    list, int -> list"""
    lista = lista_num+[n]
    list.sort(lista)
    posicao = list.index(lista,n)
    
    
    return lista[posicao+1:]