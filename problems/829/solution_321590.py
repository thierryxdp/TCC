def soma_h(N):
    """A função recebe como entrada um número inteiro 'N'.
    E deve retornar o valor H com calculado a partir do
    limite de termos definido por N. A cada número inteiro,
    1 é divido por esse mesmo número inteiro até chegar na 
    divisão de 1 pelo número N. Além disso, o valor retornado
    deve ter somente 2 casas decimais, utilizando a função
    round."""
    H=1
    for num in range(int(N)+1):
        H= H*(1/(H*num))
    return round(H,2)