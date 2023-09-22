def inverte(frase):
    'função que dada uma frase a retorna com as palavras na ordem inversa'
    frase = frase.lower()
    separar = str.split(frase)
    lista = separar[::-1]
    frase_final = str.join(' ', lista)
    frase = str.replace(frase, '!', '')
    frase = str.replace(frase, '.', '')
    frase = str.replace(frase, ',', '')
    frase = str.replace(frase, '-', '')
    frase = str.replace(frase, '?', '')
    return frase_final