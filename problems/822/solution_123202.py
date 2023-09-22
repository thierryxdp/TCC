def repetidos(num):
    """Cálculo de uma função que tem por objetivo receber uma lista de números 
    e retornar o número de vezes que um elemento da lista é igual ao elemento anterior.
    
    Parameters:
    num: Corresponde a lista de números
    
    Returns:
    Retorna o valor correspondente ao numero de repetições do número dado que:
    list -> int
    """
    repetidos=0
    while repetidos<len(num):
        if repetidos in num[repetidos]:
            list.count(num[repetidos],repetidos)
        repetidos += 1
    return repetidos-1