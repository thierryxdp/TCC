def filtra_pares(tupla):
    """ Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam. Caso não tenham elementos pares na tupla, a função retorna uma tupla vazia;
        tuple -> tuple"""
    primeiroe_par = tupla[0]%2==0 
    segundoe_par = tupla[1]%2==0 
    terceiroe_par = tupla[2]%2==0 
    quartoe_par = tupla[3]%2==0 
    numeros_pares = ()
    if primeiroe_par:
        numeros_pares = numeros_pares + primeiroe_par
    if segundoe_par:
        numeros_pares = numeros_pares + segundoe_par
    if terceiroe_par:
        numeros_pares = numeros_pares + terceiroe_par
    if quartoe_par:
        numeros_pares = numeros_pares + quartoe_par
        return numeros_pares