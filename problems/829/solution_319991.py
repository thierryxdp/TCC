def soma_h (n):
    """ funcao recebe numero n e retorna o valor de H de acordo com a formula
    entrada: int saida:float"""
    lista = list (range (1,n+1))
    H = 0
    for i in lista:
        H += round (1/i,3)
    return round (H,2)