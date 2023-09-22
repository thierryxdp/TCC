def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma, só que com as suas consoantes
em caixa alta
    str -> str
    '''
    resposta = ''
    contador = 0
    while contador < len(frase):
        if not frase[contador].lower() in 'aeiou áéíóúãõ':
            resposta += frase[contador].upper()
        else:
            resposta += frase[contador]
        contador +=1
    return resposta