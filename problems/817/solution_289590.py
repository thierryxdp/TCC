def maiores_que(lista_numeros, n):
    tamanho = len(lista_numeros)
    x = 0

    lista = ([i for i in lista_numeros if i > n])
    list.sort(lista)
    return lista

def acima_da_media(lista_numeros):
    """
    Filtra, de um lista, as notas dos alunos de uma turma que sejam maiores
    do que a média aritmética das notas.
    list -> list
    
    Parameters:
    lista_numero: Parâmetro do tipo lista (list);

    Returns:
    A nova lista com as notas que são maiores que a média das notas da turma.
    """
    
    n = (sum(lista_numeros)/len(lista_numeros))
    lista = maiores_que(lista_numeros, n)
    return lista