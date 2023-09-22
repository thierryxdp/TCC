#Função que recebe uma tupla com quatro elementos e retorna uma nova tupla apenas com os elementos pares
#tup -> tup
def filtra_pares(t):
    t0impar = t[0]%2!=0
    t0par = t[0]%2==0
    t1impar = t[1]%2!=0
	t1par = t[1]%2==0
	t2impar = t[2]%2!=0
	t2par = t[2]%2==0
	t3impar = t[3]%2!=0
	t3par = t[3]%2==0
    
    if t0impar and t1impar and t2impar and t3impar:
        return ()
    if t0par and t1impar and t2impar and t3impar:
        return t[0]
    if t0par and t1par and t2impar and t3impar:
        return t[0],t[1]
    if t0par and t1par and t2par and t3impar:
        return t[0],t[1],t[2]