#int -> float
def soma_h(N):
    #criar a variável para o resultado
    H=0
    #calcular a soma e arredondar para 2 casas decimais
    for n in range(1,N+1):
        H+=1/n
    return round(H,2)