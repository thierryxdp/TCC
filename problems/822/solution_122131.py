def repetidos(lista):
    '''Retorna o número de vezes que um elemento e seu anterior são iguais;
 list -> int'''
    i = 0
    novalista = [];
    while i<len(lista-1):
        if lista[i] == lista[i+1]:
           	list.append(novalista,True);
        else:
            list.append(novalista,False);
        i += 1
    return novalista.count(True)