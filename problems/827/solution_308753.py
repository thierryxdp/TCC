def qtd_divisores(n):
    """Função que recebe um número e retorna quantos divisores ele tem"""
    """int-->int"""
    
    resposta=0
    for i in range(1,n+1):
        if n%i==0:
            resposta+=1
    return resposta