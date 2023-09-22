def acima_da_media(lista):
    ''' funcao que dada uma lista com as notas dos alunos retorne uma lista com as notas acima da media
        list[int,int,int,int] --> list[int,int,int] '''
    
    soma_lista = sum(lista)
    variaveis  = len(lista)
    media = (soma_lista)/(variaveis)
    
    list.append(lista,media)
    list.sort(lista)
    numero_referencia = list.index(lista,media)
    del lista[:numero_referencia+1]
    
    return lista