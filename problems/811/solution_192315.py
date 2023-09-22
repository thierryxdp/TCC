def colchao(medidas,h,l):
    if( dim[1] <= h):
        return True
    else:
        return False

dim = []
teste = []

for i in range(3):#Preenche
    dim.append(medidas)

for i in range(3):#ordena
    for j in range(3):
        aux = dim[j]
        if dim[i] <= dim[j]:
            dim[j] = dim[i]
            dim[i] = aux

	
return(colchao(dim, h,l))