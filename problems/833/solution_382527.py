def conta_numero(numero,matriz):
    """Funcao que dado um numero inteiro e uma matriz de 
    inteiros de tamanho qualquer, conta e retorna quantas vezes aquele 
    numero aparece na matriz.
    Entrada: int, list 
    Saida: int
    """
    contadora = 0 
    for i in matriz:
        for elemento in i:
            if elemento == numero:
                contadora += 1
    return contadora