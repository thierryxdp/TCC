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
        if num[repetidos]==num[repetidos-1]:
            list.count(num[repetidos-1],repetidos)
        repetidos += 1
    return repetidos-1