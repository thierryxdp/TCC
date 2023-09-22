def acima_da_media(lista):
    ''' Função que, dada a lista com as notas dos alunos,utiliza as funções aplicáveis à lista e retorna outra lista com as notas maiores do que a média em ordem
lista> lista'''


    m= sum(lista)/len(lista)
    
    list.sort(lista)
    list.append(lista,m)
    list.index(lista,m)
    lista[list.index(lista,m)+1:]
    L= lista[list.index(lista,m)+1:] 
    return L