def soma_h(n):
    """Função que dado um inteiro N retorna o valor da soma de H,int-->Float"""
    cont=0
    for n in range(1,n+1):
        cont += 1/n 
    return round(cont,2)