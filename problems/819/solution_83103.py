def filtraMultiplos (lista,numero):
    '''função que dada uma lista de números e um número inteiro, devolve todos os múltiplos desse número
    list,int->list'''
    
    i=0
    multiplos = []
    inteiro = int(lista [i]/numero)
    
    while i<len (lista):
        if lista [i]/numero == inteiro :
            multiplos = multiplos + [lista [i]]
        i=i+1
    return multiplos