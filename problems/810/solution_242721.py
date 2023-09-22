def tira_pontuacao(frase):
    '''funçao que substituí pontuações na frase de entrada por espaço, retornando a frase s pontuações'''
    '''str->str'''
    texto=str.replace(frase,"."," ")
    texto=str.replace(texto,","," ")
    texto=str.replace(texto,"!"," ")
    texto=str.replace(texto,"?"," ")
    texto=str.replace(texto,"-"," ")
    texto=str.lower(texto)
    
def inverte(tira_pontuacao):
    frase2=str.lower(tira_pontuacao)
    frase2=str.split(frase2)
    frase2=list.reverse(frase2)
    return str(frase2)