def fatorial(numero):
    """ A função ao receber um número como entrada, deve
    retornar o fatorial deste número.
    Entrada: Int
    Saída: Int"""
    
    valores=list(range(1,numero+1))
    list.reverse(valores)
    i=0
    fatorial=0
    while (valores[i]-1)!=0:
        numeros=valores[i]
        fatorial= 1*numeros
        i=i+1
    return valores[0]