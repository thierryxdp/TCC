def lingua_p(palavra):
    vogais = ['a','e','i','o','u','á','é','í','ó','ú','A','E','I','O','U']
    resultado = ''
    for el in palavra:
        if el in vogais:
            resultado = resultado + (el + 'p' + el)
        else:
            resultado = resultado + el 
    return resultado.lower()