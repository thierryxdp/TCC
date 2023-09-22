'''Função que recebe uma tupla contendo 4 números inteiros e retorna apenas os pares entre eles
tupla->tupla'''
def filtra_pares(t):
    n = ()
    if (t[0]%2==0):
        n = n+ (t[0],)
        if (t[1]%2==0):
            n = n+(t[1],)
            if (t[2]%2==0):
                n = n+(t[2],)
                if (t[3]%2==0):
                    n = n +(t[3],)