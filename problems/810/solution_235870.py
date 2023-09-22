def inverte_frase(frase):
    frase= substitui_pontuacao(frase)
    frase=str.lower(frase)
    lista=str.split(frase,' ')
    lista[::-1]
    
    return str.join(' ',lista[::-1])