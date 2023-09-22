'''Função que recebe:
uma tupla (t) contendo 4 elementos int;
e retorna apenas os pares da tupla pelo sistema de filtragem;
tupla-> tupla'''
def filtra_pares(t):
    tv = ()
    if t[0]%2==0:
        tv = tv + (t[0],)
        if t[1]%2==0:
            tv = tv + (t[1],)
            if t[2]%2==0:
                tv = tv + (t[2],)
                if t[3]%2==0:
                    tv = tv + (t[3],)
                    return tupla
                filtra_pares((1,2,3,4))