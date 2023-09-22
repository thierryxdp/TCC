def filtra_pares(elementos):
    '''int,int,int,int -> int; Função que retorna os elementos pares de uma tupla de forma ordenada'''
    elementos_pares=()
    if elementos[0]%2==0:
    	elementos_pares=elementos_pares+(elementos[0],)
    if elementos[1]%2==0:
    	elementos_pares=elementos_pares+(elementos[1],)
    if elementos[2]%2==0:
    	elementos_pares=elementos_pares+(elementos[2],)
    if elementos[3]%2==0:
    	elementos_pares=elementos_pares+(elementos[3],)
    return elementos_pares