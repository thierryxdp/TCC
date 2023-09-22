def filtraMultiplos(l,n):
    '''Funçaõ que ao receber uma lista e um número, retorna uma lista
    	com apenas os números presentes na lista passada como parâemtro
        os quais são divisíveis por esse número.
        
      	list(int),int -> list'''
    i=0
    a=[]
    while i<len(l):
        if l[i]%n==0:
            a = a + [l[i]]
        i=i+1
    return a