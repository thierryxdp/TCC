def acima_da_media(lista_notas):
    '''Esta função, dada uma lista com as notas dos alunos
    (lista_notas), retorna uma lista ordenada com as notas 
    que ficaram acima da média
    list(flot) -> list(float)'''
    
    quantidade= len(lista_notas)
    media=(sum(lista_notas))/quantidade
    
    list.insert(lista_notas,1,media)
    list.sort(lista_notas)
    indice=list.index(lista_notas,media)
    n=list.count(lista_notas,media)
    acima_media=lista_notas[indice+n+1:]
    
    return acima_media