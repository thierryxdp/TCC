def inverte(frase):
    'função que dada uma frase a retorna com as palavras na ordem inversa'
    separar = str.split(frase)
    lista = separar[::-1]
    frase_final = str.foin(' ', lista)
    return frase_final