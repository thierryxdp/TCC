def inverte(frase):
    if ':' in frase:
        frase = frase.replace(':', '')
    if ';' in frase:
        frase = frase.replace(';', '')
    if '.' in frase:
        frase = frase.replace('.', '')
    if ',' in frase:
        frase = frase.replace(',', '')
    if '-' in frase:
        frase = frase.replace('-', ' ')
    if '?' in frase:
        frase = frase.replace('?', '')
    if '!' in frase:
        frase = frase.replace('!', '')
    lista = frase.split(' ')
    vezes = len(lista)+1
    lista_inv = lista[-1:-(vezes):-1]
    inverso = str.join(' ', lista_inv)
    resultado = str.lower(inverso)
    return resultado