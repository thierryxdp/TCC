def soma_h(n):
    """função que recebe um número qualquer (n) e soma a função H, tal
    que H seja a soma de 1 dividido pelo primeiro termo (1) até o termo
    n de entrada: 1 + 1/2 + 1/3 +...+ 1/n. E deve retornar o valor dessa
    soma, tal que esse resultado tenha apenas duas casas decimais;
    int->float"""
    soma = 0
    sequencia = range(1,n+1)
    for i in sequencia:
        if i<=n:
            soma = soma+round((1/i),2)
    return soma