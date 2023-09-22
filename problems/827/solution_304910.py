def qtd_divisores(numero):
    """Função que calcula a quantidade de divisores um número possui, sendo os dados de entrada um número inteiro
    e na saída outro número inteiro"""
    contagem=0
    for item in range(1,numero+1):
        if numero%item ==0:
            contagem+=1
    return contagem