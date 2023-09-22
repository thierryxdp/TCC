def soma_h(N):
    """ Essa função retorna a soma de 1 dividido por todos os números naturais sem o zero até o número inteiro de entrada n
    int--> float"""
    soma=0
    for n in range (1,N):
        adicionando=1/n
        soma= soma + 1/n
    return soma