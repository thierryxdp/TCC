def faltante(lista):
    """
    Retorna um número inteiro que pertence ao intervalo, mas não pertence a lista original.
    list -> int
    """
    somaPA=0
    i=0
    while i<len(lista)+1:
        somaPA=somaPA + (i+1)
        i=i+1
    return somaPA-sum(lista)