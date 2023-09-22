def acima_da_media(lista):
    '''função que, dada uma lista com as notas dos alunos, retorne as notas
    acima da média.
    list -> list'''
    soma_notas = sum(lista)
    quantos_alunos = len(lista)
    media = soma_notas/quantos_alunos
    
    lista_com_n = lista.insert(0,media) #insere a nota média na lista
    lista_ordenada = lista.sort() #ordena a nova lista
    i = lista.index(media) + 1 #indice +1 (soma 1 para facilitar o fatiamento a seguir)
    del lista_ordenada[:i] 
    return lista_ordenada