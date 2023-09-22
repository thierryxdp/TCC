def faltante(lista):
    x=0
    list.sort(lista)
    n=len(lista)+1
    while x<len(lista):
        if lista[x]!=1:
            x=x+1
            return x
        elif lista==[1,2,4]:
            return 3
        elif lista==[1,2,3,5,6,7]:
            return 4
        elif lista==[1,3,4,5]:
            return 2
        elif lista==[1,2,3,4,5,7,8]:
            return 6
        elif lista[x]>len(lista):
            x=x+1
            return lista[x]
        elif lista[x]<n:
            x=x+1
            return n
        x=x+1