#4
def maiores(lista_numero,n):
    """Funcao que, dados uma lista e um numero inteiro n, retorna uma nova lista
    com todos os numeros maiores que n;
    Entrada: list, int
    Saida: list"""
    
    lista = lista_numero + [n]
    list.sort(lista)
    posicao= list.index(lista,n)
    return lista[posicao+1:]
#5
def acima_da_media(lista):
    """Funcao que recebe uma lista com as notas dos alunos de uma turma e retorna
    uma lista ordenada com as notas que ficaram acima da media:
    Entrada: list
    Saida: list"""

    media = sum(lista)/len(lista)
    if media in lista:
        qtd = list.count(lista,media)
        lista = maiores(lista,media)
        lista = lista[qtd:]
        return lista
    else:
        return maiores(lista,media)