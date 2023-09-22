def conta_numero(numero,matriz):
    '''Retorna quantas vezes um número aparece em uma matriz
    entrada: float, list
    saída: int
    '''
    
    # Contando quantas vezes o número aparece em cada coluna
    
    vezesporcoluna=[]
    for coluna in matriz:
        vezesnacoluna=list.count(coluna,numero)
        list.append(vezesporcoluna,vezesnacoluna)
        
    # Definindo quantas vezes o número aparece na matriz
    
    quantasvezes=sum(vezesporcoluna)
    return quantasvezes