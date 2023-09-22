def soma_h(n):
    """Funcao que recebe o numero n de termos de uma soma e retorna o valor total dessa soma. int=>int/float"""
    valorh=0
    for x in range(n+1):
        if x!=0:
            valorh= valorh+1/x
    return valorh