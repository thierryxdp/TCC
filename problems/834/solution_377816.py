def media_matriz(matriz):
    """essa funcao calcula que dada uma matriz de inteiros nao vazia, retorna a  media de todos os numeros da matriz(com exatamente duas casas decimais de precisao; list-> float"""
    num=0
    n=0
    for i in matriz:
        num=num+sum(i)
        n=n+len(i)
    return round(num/n,2)