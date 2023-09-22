def conta_numero(numero,matriz):
    """Funcao que dado um numero inteiro e uma matriz de tamanho qualquer retorna quantas vezes esse numero inteiro aparece na matriz. int,list=>int"""
    acheiatequeenfim=0
    for x in matriz:
        for y in x:
            if numero==y:
                acheiatequeenfim=acheiatequeenfim+1
    return acheiatequeenfim