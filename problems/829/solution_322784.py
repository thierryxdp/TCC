def soma_h(n):
"""FUNÇÃO QUE RETORNA O VALOR DE H COM N TERMOS,
    SENDO ESTE PASSADO COMO ENTRADA"""
    soma=0
    for i in range(1,n+1):
        soma+=1/i
    return round(soma,2)