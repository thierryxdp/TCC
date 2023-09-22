def retira_pontuacao(frase):
    '''funçao que substituí pontuações na frase de entrada por espaço, retornando a frase s pontuações'''
    '''str->str'''
    str.lower(frase)
    texto=str.replace(frase,"."," ")
    texto=str.replace(texto,","," ")
    texto=str.replace(texto,"!"," ")
    texto=str.replace(texto,"?"," ")
    texto=str.replace(texto,"-"," ")
    return texto