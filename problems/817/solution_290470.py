def maiores(lista,n):
    lista.append(n+1)
    lista.sort()
    i = lista.index(n+0.001)
    return lista[i+0.001:]
def acima_da_media(lista):
    """
    Função que recebe uma lista de notas de uma turma e retorna 
    uma lista das notas que ficaram acima da média
    
    list ---> list
    """
    media = sum(lista)/len(lista)
    return maiores(lista,media)