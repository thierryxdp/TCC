def repetidos(lista):
    i=0
    resultado=0
    while i<len(lista):
        if lista[i] == lista[(1+i)]:
        	resultado=resultado+1
        if lista[i] != lista[(i+1)]:
        	resultado=resultado+0
        i=i+1
    return i