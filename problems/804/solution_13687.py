def k_pares(k):
    """Recebe uma tupla que contenha quatro números inteiros
e através da função e_par retorna uma nova tupla contendo somente
os números que são pares.
tuple -> tuple
"""
    e_par = k%2 == 0
    
    tupla = ( )
    if e_par(k[0]):
        tupla = tupla + (k[0],)
    if e_par(k[1]):
        tupla = tupla + (k[1],)
    if e_par(k[2]):
        tupla = tupla + (k[2],)
    if e_par(k[3]):
        tupla = tupla + (k[3],)
    	return tupla