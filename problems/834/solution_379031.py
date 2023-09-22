def media_matriz(matriz):
    '''Retorna a media de todos os numeros da matriz com exatamente duas casas decimais de precisão
    list -> float'''
    comp=0
    soma=0
    for i in matriz:
        comp = comp + len(i)
        soma = soma + sum(i)
        return round(soma/comp,2)