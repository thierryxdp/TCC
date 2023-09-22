def soma_h(N: int) -> float:
    """Essa função, dado um número inteiro N,
    calcula e retorna sua soma H com precisão de duas casas decimais.
    Sendo a Soma H determinada pela soma de frações com  
    todos os numeradores iguais a 1 e os denominadores de 1 a N"""
    H = 0
    for i in list(range(1,N+1)):
        H += 1/i
    return round(H,2)