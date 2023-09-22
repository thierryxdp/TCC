def repetidos(lista):
    '''função que recebe uma lista de número e retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    tipo de entrada: list
    tipo de saída: int '''
    x=0
    rep=0
    while x< len(lista)-1:
        if lista[x]==lista[x+1]:
            rep+=1
        x+=1
    return rep