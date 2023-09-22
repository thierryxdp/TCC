def repetidos(num):
    """Cálculo de uma função que tem por objetivo receber uma lista de números 
    e retornar o número de vezes que um elemento da lista é igual ao elemento anterior.
    
    Parameters:
    num: Corresponde a lista de números
    
    Returns:
    Retorna o valor correspondente ao numero de repetições do número dado que:
    list -> int
    """
    i=0
    repetidos=0
    while i<len(num):
        if num[i]==[i-1]:
            repetidos=list.count(i-1)
        i+=1
    return repetidos-2