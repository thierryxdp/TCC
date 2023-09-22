import array
def retira_pontuação(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    return str.replace(frase,array('.',',',';',':','-','!','?','...'),' ')