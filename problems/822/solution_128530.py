def repetidos(numero):
    resultado=0
    while len(numero)>1:
        popped1=numero.pop()
        popped2=numero.pop()
        if popped1=popped2:
            resultado +=1
            numeros.append(popped2)
        else:
            numeros.append(popped2)
     return resultado