def melhor_volta(matriz):
    '''Calcula e retorna uma tupla a qual mostrara a melhor volta, o piloto que a fez e em qual tentativa isso ocorreu
       parameters:
       matriz: Matriz 6x10 inicial com numeros diferentes
       list->tuple'''
    a=min(matriz[0])
    b=min(matriz[1])
    c=min(matriz[2])
    d=min(matriz[3])
    e=min(matriz[4])
    f=min(matriz[5])
    lista=[a,b,c,d,e,f]
    for i in range(len(matriz)):
        if min(lista) in matriz[i]:
            pos=list.index(matriz[i],min(lista))
            i+=1
            return (i,min(lista),pos+1)