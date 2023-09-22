def soma_h(N):
    """Função que retorna o resultado de uma soma de termos, onde o último
    depende do valor "N" fornecido."""
    """int-->float"""
    resultado=[]
    termos=list(range(1,N+1))
    for elemento in termos:
        resultado=resultado+[1/elemento]
    return round(sum(resultado),2)