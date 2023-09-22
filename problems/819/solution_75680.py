def filtraMultiplos(lista,num):
    """ Para filtrar e retornar os numeros multiplos de número,
    na mesma ordem da lista original, digite;
    int,int-> int"""
    
    l=[]
    i=0
    while i < len(lista):
        if lista[i]%num==0:
            l.insert(i,lista[i])
        i+=1
    return l