def conta_frases(texto):
    '''Dado um texto armazenado em uma string, a função retorna o número de frases que aparecem nesse texto; str->int'''

    texto = str.replace(texto,"?",".")
    texto = str.replace(texto,"!",".")
    texto = str.replace(texto,"...",".")
    
    lista = str.split(texto,".")
    
    total = len(lista)
    
    return total - 1