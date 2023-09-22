def inverte(frase):
    '''inverte a ordem das palavras em uma frase
    str->str'''
    frase=frase.replace(";","#")
    frase=frase.replace("!","#")
    frase=frase.replace("?","#")
    frase=frase.replace(".","#")
    frase=frase.replace(":","#")
    frase=frase.replace(",","#")
    frase=frase.replace("-","#")
    frase=str.replace(frase,"#"," ")
    str.split(frase)
    return frase[::-1]