def conta_numero(numero,matriz):
    '''Função que dado como entrada um numero inteiro e uma matriz de inteiros de qualquer ordem irá contar e retornar quantas vezes aquele aparece na matriz. Utiliza-se laços aninhados For para : percorrer as linhas da matriz e para cada elemento da linha percorrido é estabelecida a condição que quando o numero for igual a variável usada para percorrer os elementos da linha, a variável cont irá ser atualizada somando mais 1
    int,matriz>> int'''
    cont=0
    for i in matriz:
        for j in i:
            if numero==j:
                cont= cont + 1
        return cont