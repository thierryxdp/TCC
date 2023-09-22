def conta_numero(numero,matriz):
    '''
        Função que dado um inteiro qualquer e uma matriz, retorna a quantidade
        ocorrências do numero inteiro.
        int,list -> int
    '''
    contador=0
    for i in matriz:
        if numero in i:
            contador=contador + i.count(numero)
    return contador