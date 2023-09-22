def inverte(frase):
    '''Esta funçao inverte a posiçao das palvras na frase
    string ==> string '''
    x = retira_pontuacao(frase)
    y = str.split(str.strip(x," ")," ")
    list.reverse(y)
    z = str.join(" ",y)
    
    return str.lower(z)