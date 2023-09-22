def soma_h(N):
    '''Retorna a soma dos inversos dos inteiros 
    de 1 até N (positivo e inteiro) com aproximacao
    de 2 casas decimais
    int -> float'''
    lista_inversos = []
    for inteiro in range(N):
        inverso = (inteiro+1)**(-1)
        list.append(lista_inversos,inverso)
    soma = 0
    for inversos in lista_inversos:
        soma = soma + inversos
    return round(soma,2)