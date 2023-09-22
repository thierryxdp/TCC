def faltante(lista):
    '''diz qual o numero faltando na lista. list->int'''
    i=0
    numeros=[0,1,2,3,4,5,6,7,8,9]
    a=[]
    while i<len(lista):
        if nuemros[i] not in lista:
            a.append(numeros[i])
        i=i+1
    return a[-1]