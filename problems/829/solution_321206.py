def soma_h(N):
    "retorna o valor de H com N termos retornando o resultado com 2 casas decimais"
    soma = 0
    for x in range(1,N+1):
        soma = soma + 1/x
    return round(soma,2)