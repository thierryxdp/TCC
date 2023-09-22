def conta_numero(numero,matriz):
    """ Retorna quantos numeros existem dentro da matriz; int,list -> int """
    c=matriz;
    lista=[];
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if c[i][j]==numero:
                list.append(lista,1);
            else:
                list.append(lista,0);
    return lista.count(1)