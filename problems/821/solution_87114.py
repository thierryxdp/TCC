def fatorial(numero):

    """ A ideia por trás do fatorial é termos sucessivas
        multiplicações de números inteiros e positivos.
        Por isso, usaremos a ideia de loop e multiplicaremos
        cada nova iteração pelo resultado da iteração antiga.

        Os acumuladores funcionam da forma que o fatorial comece em 1(fatorial
        de 1) e o valor de i comece em 2 (que é o valor de 2!, pois estamos
        multiplicando o valor do fatorial, 1 pelo valor de i,2. Resultando
        em 1*2. Funciona da mesma forma para as iterações seguintes. Ou seja,
        a função while começa para o fatorial de 2.
        Obs: Não há resultado para números negativos e por definição,
        fatorial de 0 é 1, e o fatorial de 1 é o próprio 1.

        int -> int
    """

    fatorial = 1
    i = 2

    if numero<0:
        return 'Não há fatorial de números negativos'
    
    elif numero == 0 or numero == 1:
        return 1
    
    while i <= numero:
        
        fatorial = fatorial*i
        i = i + 1

    return fatorial