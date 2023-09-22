def filtra_pares(tupla):
    "Reecebe uma tupla com 4 elementos inteiros e retorna uma tupla contendo apenas os elementos pares da tupla original na mesma ordem; str->str."""
    if tupla[0]%2==0:
        t0=(t[0],)
    else:
        t0=()
    if tupla[1]%2==0:
        t1=(t[1],)
    else:
        t1=()
    if tupla[2]%2==0:
        t2=(t[2],)
    else:
        t2=()
	if tupla[3]%2==0:
        t3=(t[3],)
    else:
        t3=()
	return t0,t1,t2,t3