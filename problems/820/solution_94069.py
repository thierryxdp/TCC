def posLetra(frase,letra,numero): #Recebe uma frase, a letra observada e o numero de vezes que quer que ela apareça
    frasefinal = []
    for let in frase:
        frasefinal.append(let)
    contador = 0
    posicao = 0
    numero_de_ocorr = list.count(frasefinal, letra)
    if numero_de_ocorr < numero:
        return -1 #Caso o número de ocorrencias seja menor que a desejada, o valor retornado é -1
    for let in frase:
        if let == letra:
            contador = contador + 1
            if contador == numero:
                return posicao #Procura a posição da ultima ocorrencia desejada da letra
        posicao = posicao + 1