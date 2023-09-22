def soma_h (N):
    """A função calcula o somatório de 1+1/N com N sendo um numero inteiro e positivo dado no 
    parametro; 
    int-> float"""
    somatorio = 1
    for x in range (2, N+1):
        somatorio = 1 + 1/x
    return round(somatorio, 2)