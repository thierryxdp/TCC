def filtra_pares(tupla):
    "Reecebe uma tupla com 4 elementos inteiros e retorna uma tupla contendo apenas os elementos pares da tupla original na mesma ordem; str->str."""
    if tupla[0]%2==0:
        t0=(tupla[0],)
    if tupla[1]%2==0:
        t1=(tupla[1],)
	if tupla[2]%2==0:
        t2=(tupla[2],)
    if tupla[3]%2==0:
        t3=(tupla[3],)
    return t0,t1,t2,t3