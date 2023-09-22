def maiores (lista,n):
    '''
    Função retorna todos os numeros maiores
    que o valor dado.
    list,int -> list
    '''
    lista.append(n+1)
    lista.sort()
    posicao = lista.index(n+1)
    return lista[posicao+1:]

def acima_da_media (list_nota):
    '''
    A função retorna uma lista com 
    a nota dos alunos acima
    da media.
    list -> list
    '''
    notas = sum(list_notas)
    media = notas/len(list_notas)
    return maiores(list_notas,media)