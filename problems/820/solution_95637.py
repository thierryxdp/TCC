def posLetra(frase, letra, numero):
    '''função que recebe umma frase uma letra e um numero e retorna em 
    qual posição a letra recebida aparece na frase na ocorrencia informada'''
    contador = 0
    ocorrencia = 0
    while (frase[contador] != letra and ocorrencia != numero):
        contador += 1
        if frase[contador] != letra:
            ocorrencia += 1
    return contador