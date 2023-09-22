def retira_pontuacao(frase):
    ''' função que retorna a frase onde toda pontuação sao
    	substituidos por espaço.
        str ---> str '''
    sempont = str.replace(frase, '.', ' ')
    sempont = str.replace(sempont, '?', ' ')
    sempont = str.replace(sempont, ',', ' ')
    sempont = str.replace(sempont, '!', ' ')
    sempont = str.replace(sempont, '-', ' ')
    sempont = str.replace(sempont, ':', ' ')
    sempont = str.replace(sempont, ';', ' ')
    return sempont