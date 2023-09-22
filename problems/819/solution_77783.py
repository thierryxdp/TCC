def filtraMultiplos(lista,n):
    '''funcao que recebe uma lista de numeros e um numero n e retorna
    os multiplos desse;
    list,int->list'''
    
    i=0
    nova=[]
    while i<len(lista):
        if lista[i]%n==0:
            nova[i]=lista[i]
        i=i+1
    return nova