def conta_numero(numero,matriz):
    """ Retorna quantos numeros existem dentro da matriz; int,list -> int """
    c=matriz;
    for i in range(len(matriz)):
        a=0;
        for j in range(len(matriz[0])):
            if c[j][i]==numero:
                a=a+1;
            else:
                a=a
    return lista