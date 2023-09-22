def repetidos(lista):
    '''essa lista tem como objetivo verificar se existe na lista números
    repetidos, e compara sempre com o seu anterior, e dar como resposta
    o número de repetições que ocorre'''
    '''list -> int'''
    
    i= 0
    rep = 0
    pos1 = lista[i - 1] 
    pos2 = lista[i]
    while i < (len(lista)-1):
        if pos1 == pos2:
            rep = rep + 1
        i = i+1
        pos1 =lista[i - 1]
        pos2 = lista[i]
        
    return rep