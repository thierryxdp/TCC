def conta_numero(numero,matriz):
    """Função que dado um número inteiro e uma matriz retorna a quantidade
    de vezes que aquele numero aparece;lista,int-->int"""       
    rep=str.split(matriz)
    ocorrencias=[]
    for x in rep:
        qtd=str.count(rep,numero)
        list.append(ocorrencias,qtd)
    return ocorrencias