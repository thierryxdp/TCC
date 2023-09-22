def filtraMultiplos (lista,numero):
    '''função que dada uma lista de números e um número inteiro, devolve todos os múltiplos desse número
    list,int->list'''
    
    i=0
    multiplos = []
    divisao = lista [i]/numero
    inteiro = int(divisao)
    
    while i<len (lista):
        if divisao == inteiro :
            multiplos = multiplos + lista [i]
        i=i+1
    return multiplos