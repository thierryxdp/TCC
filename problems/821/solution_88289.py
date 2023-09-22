def fatorial(numero):
    """ A função ao receber um número como entrada, deve
    retornar o fatorial deste número.
    Entrada: Int
    Saída: Int"""
    
    valores = list(range(1,numero+1))
    i=0
    fatorial=0
    while (valores[i]-1)!=0:
        numeros=valores[i]
        fatorial=fatorial+numeros
    i=i+1
    return valores=list(range(1,numero+1))