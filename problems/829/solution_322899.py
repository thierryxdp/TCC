def soma_h(N):
    """Função que recebe um numero inteiro e retorna a soma deste com um sobre seus antecessores;
    int--float"""
    soma = 0
    for i in range(1,N+1):
        soma = soma + (1/i)
    return round(soma,2)