def primo (numero):
    lista=[]
    for i in range(1,numero+1):
        if numero%i==0:
            lista.append(i)
    if len(lista)<=2:
        return True
    else:
		return False