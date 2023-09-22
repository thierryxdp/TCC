def soma_h(n):
    """ Função que calcula o valor de 'n' termos,
    no qual 1 + 1/2 + 1/3 1/4... até 'n', e retorna o valor
    em até duas casas decimais.
    Entrada: int
    Saída: int/float """
    soma = 0
    for x in range(1,n+1):
        soma = soma + 1/x
    return round(soma,2)