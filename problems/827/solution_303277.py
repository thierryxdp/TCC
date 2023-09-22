def qtd_divisores(n):
    """Essa função calcula a quantidade de divisores dado um número n
    . Como entrada temos um número qualquer n e como saída temos a
    quantidade de divisores de números;
    int->int"""
    listadivisores=[]
    quantidadedivisores=0
    divisores=list(range(1,n+1,1))
    for i in divisores:
        if n%i==0 and n>0:
            listadivisores.append(i)
            quantidadedivisores=len(listadivisores)
    return quantidadedivisores