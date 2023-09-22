#Start your python function here
def filtra_pares(Tupla):
    '''Função que dados quatro elementos inteiros
    ocorre o retorno de uma nova tupla contendo
    apenas os elementos pares da tupla original, 
    respectivamente.
    Parâmetros de Entrada: Tupla(int, int, int, int)
    Valores de Saída: Tupla (n_int)'''
    
    Tupla = w, x, y, z
    resposta = ()
    
    W = bool (w/2 == w//2)
    X = bool (x/2 == x//2)
    Y = bool (y/2 == y//2)
    Z = bool (z/2 == z//2)
    
    if W == True:
        resposta = resposta + (w,)
    if X == True:
        resposta = resposta + (x,)
    if Y == True:
        resposta = resposta + (y,)
    if Z == True:
        resposta = resposta + (z,)
        return resposta