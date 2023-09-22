def filtramultiplos(lista,n):
    '''função que recebe uma lista de números e um número e retorna 
    outra lista com todos os elementos da lista original que são
    divisíveis por N. list, int -> list'''
    i=0
    nova=[]
    while i < len(lista):
        if lista[i] %n==0:
            nova=nova+[lista[i],]
        i+=1
    return nova