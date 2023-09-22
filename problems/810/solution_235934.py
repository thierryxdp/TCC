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
    s=str.replace(frase,"#"," ")
    str.split(s)
    return str.join(,s,-1)