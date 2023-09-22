def conta_frases (frase):
    '''
    função que conta o número de frases do texto dado como parâmetro
    str-->int
    '''
    texto1= str.replace(frase,"...","123")
    texto2= str.replace(texto1,".","123")
    texto3= str.replace(texto2,"!","123")
    texto4= str.replace (texto3,"?","123")
    return str.count(texto4,"123")