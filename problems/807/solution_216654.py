def conta_frases(texto):
    '''dada a entrada de um texto string, a função retorna
    quantas frases há nele; 
    str-> int'''
    texto = str.replace(texto, "...","#")
    texto = str.replace(texto, ".","#")
    texto = str.replace(texto, "!","#")
    texto = str.replace(texto, "?","#")
    return len(str.split(texto,"#")) - 1