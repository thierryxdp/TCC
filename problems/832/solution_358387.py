def eh_quadrada(matriz):
    """Dada uma matriz, retorna com true caso seja quadrada 
e false caso não seja.
list -> bool"""
    cont=0
    for i in range(len(matriz)-1):
        if matriz[i]==matriz[i+1]:
            cont+=1
  	return cont==len(matriz)