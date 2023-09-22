def filtraMultiplos(lista,numero):
    resultado=[]
    x=0
    while x <= len(lista)-1:
        if lista[x] % numero==0:
            y=lista[x]
            list.append(resultado,y) 
            x=x+1
            elif x<= len(lista):
                lista[x]% numero !=0
                x=x+1
            return resultado