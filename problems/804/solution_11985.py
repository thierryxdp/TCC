def filtra_pares(tupla):
	'''funcao que filtra numeros pares dada
    uma tupla como parametros'''
    pares=()
    if elementos[0]%2==0:
        pares=pares+(tupla[0],)
    if elementos[1]%2==0:
        pares=pares+(tupla[1],)
    if elementos[2]%2==0:
        pares=pares+(tupla[2],)
    if elementos[3]%2==0:
        pares=pares+(tupla[3],)
    return pares