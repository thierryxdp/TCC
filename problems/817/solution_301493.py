def acima_da_media(lista_notas):
    '''Funcao que dada uma lista com as notas dos alunos
    retorna uma lista ordenada com as notas acima da media.
    Parametros:
    list
    Saida:list
    '''
    h=[]
    for lista_notas in lista_notas:
        if lista_notas > sum(lista_notas):
            h.append(lista_notas)
           
        
    return h