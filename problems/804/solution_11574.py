def filtra_pares (tupla):
    tupla_n = ()
	if tupla[0]%2==0:
        tupla_n=tupla_n+(tupla[0],)
    if tupla[1]%2==0:
        tupla_n=tupla_n+(tupla[1],)
    if tupla[2]%2==0:
        tupla_n=tupla_n+(tupla[2],)
    if tupla[3]%2==0:
        tupla_n=tupla_n+(tupla[3],)     
    return tupla_n
'''dado uma tupla com 4 elementos, retorna uma nova
tupla com os elementos pares
int->tuple'''