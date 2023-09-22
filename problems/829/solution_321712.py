def soma_h(n):
    resposta = 0
    for numero in range(1,n+1):
        resposta += 1 / numero
    return round(resposta, 2)