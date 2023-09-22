def filtra_pares(tupla):
    """ Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam. Caso não tenham elementos pares na tupla, a função retorna uma tupla vazia;
        tuple -> tuple"""
    primeiroe_par = tupla[0]%2==0 
    segundoe_par = tupla[1]%2==0 
    terceiroe_par = tupla[2]%2==0 
    quartoe_par = tupla[3]%2==0 
    numeros_pares = ()
    if primeiroe_par:
        numeros_pares = numeros_pares + (tupla[0],)
    if segundoe_par:
        numeros_pares = numeros_pares + (tupla[1],)
    if terceiroe_par:
        numeros_pares = numeros_pares + (tupla[2],)
    if quartoe_par:
        numeros_pares = numeros_pares + (tupla[3],)
        return numeros_pares