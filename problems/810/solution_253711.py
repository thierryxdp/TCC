def inverte(x=""):
    '''Esta função retorna uma determinada frase em sua ordem inversa
    de palavras
    assinatura str -> str'''
    x=x.repalce(".","").replace(";","").replace(",","").replace("-"," ").replace(:,"").replace("?","")
    x=x.split(" ")
    return str(" ").join(x[::-1])