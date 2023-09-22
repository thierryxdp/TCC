def conta_numero(numero,matriz):
    """Função que dado um numero e uma matriz retorna quanta vezes o numero
    aparece na matriz"""
    totaln=0
    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
                totaln+=1
    return totaln