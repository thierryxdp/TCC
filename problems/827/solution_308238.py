def qtd_divisores(N):
    "RECEBE UM NUMERO E RETORNA A QUANTIDADE DE DIVISORES DESTE NUMERO"
    "ENTRADA: INT. SAIDA:INT."
    divisores=0
    for i in range(1, N+1):
        if N%i==0:
            divisores=divisores+1
        else:
            divisores=divisores+0
    return divisores