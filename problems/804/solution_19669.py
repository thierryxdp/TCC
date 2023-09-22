def filtra_pares (tupla):
    '''função que recebe um tupla e devolve somente seus numeros pares; tupla->tupla'''
	a = (tupla[0]%2==0)
    b = (tupla[1]%2==0)
    c = (tupla[2]%2==0)
    d = (tupla[3]%2==0)
    if (a,b,c,d)==True:
        return (a,b,c,d)