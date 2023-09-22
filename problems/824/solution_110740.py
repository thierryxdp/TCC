def uppCons(frase):
    ''' Função que retorna uma frase dada com todas as consoantes maiúsculas '''
    ''' str -> str '''
    i = 0
    resposta = ''
    while i < len(frase):
        if str.upper(frase[i]) not in 'AEIOUÁÉÍÓÚÃÕÂÊÎÔÛ':
            i = i+1
            resposta = resposta + str.upper(frase[i])
        else:
            if str.upper(frase[i]) in 'AEIOUÁÉÍÓÚÃÕÂÊÎÔÛ':
                i = i+1
                resposta = resposta + frase[i]
    return resposta