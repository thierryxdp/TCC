def conta_numero(numero,matriz):
    '''Retorna quantas vezes um número aparece em uma matriz
    entrada: float, list
    saída: int
    '''
    vezesporcoluna=[]
    for coluna in matriz:
        vezesnacoluna=list.count(coluna,numero)
        list.append(contavezes,vezesnacoluna)
    quantasvezes=sum(vezesporcoluna)
    return quantasvezes