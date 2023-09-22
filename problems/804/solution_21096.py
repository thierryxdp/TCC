#Start your python function here
# Função que recebe uma tupla, necessariamente de quatro elementos,
# como parâmetro, retornando uma nova tupla contendo apenas os 
# elementos pares.
# tup -> tup
def filtra_pares(s):
    Y=()
    if (s[0]%2==0):
    	Y=(s[0],)
    if (s[1]%2==0):
    	Y=Y+(s[1],)
    if (s[2]%2==0):
    	Y=Y+(s[2],)
    if (s[3]%2==0):
        Y=Y+(s[3],)
	return Y