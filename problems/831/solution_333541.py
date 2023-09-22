def lingua_p(palavra):
    minuscula = palavra.lower()
    vogais = "aáeéiíoóuú"
    
    '''
    for letra in vogais:
        minuscula = minuscula.replace(letra, letra + 'p' + letra)
    '''
    
    contador = 0
    while contador < len(vogais):
        letra = vogais[contador]
        minuscula = minuscula.replace(letra, letra + 'p' + letra)
        contador = contador + 1
    
    return minuscula