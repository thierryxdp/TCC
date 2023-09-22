def qtd_divisores(numero):
    ndd=o
    for n in range (1,numero+1):
        if numero %n==0:
            ndd=ndd+1
            return ndd