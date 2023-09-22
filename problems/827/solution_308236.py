def qtd_divisores(N):
    "RECEBE UM NUMERO E RETORNA SEUS DIVISORES"
    "ENTRADA: INT. SAIDA:INT."
    divisores=[]
    for i in range(1, N+1):
        if N%i==0:
            divisores=divisores+i
    return divisores