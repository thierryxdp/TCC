def repetidos(lista):
    '''
       Função que recebe uma lista de numeros (lista) e
       retorna o numero de vezes que um elemento da lista é
       igual ao elemento anterior
       list -> int
    '''
    i=0
    rep=0
    while i<len(lesta):
        if lista[i]==lista[i+1]:
            rep=rep+1
        i=i+1
    return rep