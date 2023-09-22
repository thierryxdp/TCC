#Funcao que calcula e retorna o valor H com N termos onde N é int e dado como entrada
#Entrada int > retorno float.

def soma_h(N):
    i = 1
    H = 0
    while i<=N:
        H = H + 1/i
        i = i + 1
    return round(H, 2)