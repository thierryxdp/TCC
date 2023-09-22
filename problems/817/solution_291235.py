def maiores (lista, n):
    """funçao que recebe uma lista de numeros inteiros e um numero n e retorna a lista apenas com todos os numeros maiores do que o numero n;
    entrada: list, int
    saida: list."""
    
    if n not in lista:
        list.append (lista, n)
    list.sort (lista)
    
    indice = list.index (lista, n)    
    listaf = lista[indice +1:]
    
    return listaf

def acima_da_media (lista_notas):
    """funçao que recebe uma lista com as notas dos alunos de uma turma e retorna uma lista ordenada com as notas acima da media da turma;
    entrada: list;
    saida: list."""
    
    mediaT = sum (lista_notas) / len (lista_notas)
    
    return maiores (lista_notas, mediaT)