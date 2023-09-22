def qtd_divisores(numero):
    """Recebe um número e retorna quantos divisores aquele
    número possui.
    Assinatura: floar -> int"""
    divisores=[]
    contador=0
    if numero == 0:
        return 0
    while contador<=numero:
        contador+=1
        if numero%contador == 0:
            divisores.append(contador)
    return len(divisores)