def repetidos(l):
    ''' Essa função ao receber como valor de entrada uma lista de número, ela retornara o número de vezes que um elemento da lista é igual ao elemento anterior'''
    '''list -> int'''
    
    rep = 0
    i = 0
    
    for i in range (len(l)-1):
        if l[i] == (l[i+1]):
            rep = rep + 1
            i = i + 1
            return rep