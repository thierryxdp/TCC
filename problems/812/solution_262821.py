def retira_pontuacao(frase):
    '''Funçao que dada um frase de entrada retorna
    sem os caracteres de pontuação
    str -> str'''
    sempont=frase
    remover=['.',',','?','!','-',':',';']
    for x in remover:
        sempont = sempont.replace(x,' ')
    return sempont