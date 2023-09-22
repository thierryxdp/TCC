def fatorial(numero):
    """Função que calcula o fatorial de um número usando recursão, sendo o dado de entranada um número inteiro
    e na saída o fatorial desse número."""
    #if foi utiizado como condição de parada
    if numero==1 :
        return 1
    return numero*fatorial(numero-1)