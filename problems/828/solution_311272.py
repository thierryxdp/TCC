def primo(n):
    lista=[2,3,5,7]
    lista2=[]
    for c in len(lista):
        if n%lista[c]==0:
            lista2.append(c)
           	
    if len(lista2)>0:
        return False
    else:
        return True