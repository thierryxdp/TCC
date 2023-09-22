def posLetra(frase, letra, numero):
    '''função que recebe umma frase uma letra e um numero e retorna em 
    qual posição a letra recebida aparece na frase na ocorrencia informada'''
    contador = 0
    while frase[contador] != letra:
        catador += 1
    return frase[contador]