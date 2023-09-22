def uppCons(frase):
    ''' Função que retorna uma frase dada com todas as consoantes maiúsculas '''
    ''' str -> str '''
    i = 0
    resposta = ''
    while i < len(frase):
        if str.upper(frase[i]) not in 'AEIOUÁÉÍÓÚÃÕÂÊÎÔÛ':
            resposta = resposta + str.upper(frase[i])
            i = i+1
        else:
           	if str.upper(frase[i]) in 'AEIOUÁÉÍÓÚÃÕÂÊÎÔÛ':
                resposta = resposta + frase[i]
                i = i+1
    return resposta