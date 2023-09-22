def retira_pontuacao(frase):
    ''' A função substitui caracteres de pontuação de uma frase por espaços.
    Retornando a frase editada.
    	str -- > str'''
    
    caracteres = ['-',',','.',';',':','?','...','!']
    for i in caracteres:
        frase = frase.replace(i, ' ')
    return frase