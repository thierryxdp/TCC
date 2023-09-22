def inverte(x=""):
    '''
    função que recebe uma frase e a retorna invertida, 
    sem letra maiuscula e sem pontuação
    str->str
    '''
    x=x.replace(".","").replace(";","").replace(",","").replace("-"," ").replace(":","").replace("?","").replace("!","").replace("/","").lower()
    x=x.split(" ")
    return str(" ").join(x[::-1])