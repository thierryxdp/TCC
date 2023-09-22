def inverte(x=""):
    '''
       funcao que retorna uma frase na ordem inversa
       sem pontuacao
    
    ''' 
    x=x.replace(".","").replace(";","").replace(",","").replace("-"," ").replace(":","").replace("?","").replace("!","").replace("/","").lower()
    x=x.split(" ")
    return str(" ").join(x[::-1])