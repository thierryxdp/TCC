def conta_numero(numero,matriz):
    """ dado um numero e uma matriz retorna quantas vezes 
    esse numero aparece na matriz. int,matriz--->int"""
    dados=[]
    for x in range(len(matriz)):
        if numero in matriz[x]:
            var=list.count(matriz[x],numero)
            list.append(dados,var)
    retorno=int(sum(dados))
    return retorno