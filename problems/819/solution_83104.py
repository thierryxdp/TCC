def filtraMultiplos (lista,numero):
    '''função que dada uma lista de números e um número inteiro, devolve todos os múltiplos desse número
    list,int->list'''
    
    i=0
    multiplos = []

    while i<len (lista):
        if lista [i]/numero == int(lista [i]/numero) :
            multiplos = multiplos + [lista [i]]
        i=i+1
    return multiplos