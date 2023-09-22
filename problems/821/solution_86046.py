def fatorial(numero):
    """Essa função retorna o fatorial do número informado.
    Como entrada temos um número, e como saída temos o fatorial do
    numero;
    int->int"""
    indice=0
    fatoracao=list(range(1,numero+1,1))
    list.reverse(fatoracao)
    multiplicacao=1
    while indice<len(fatoracao):
        multiplicacao=multiplicacao*fatoracao[indice]
        indice+=1
    return multiplicacao