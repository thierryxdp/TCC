def inverte(frase):
    '''dada uma frase, retorna outra com as palavras na ordem inversa
    str -> str'''
    
    frase = str.lower (frase)
    frase = str.replace (frase, '-', ' ')
    frase = str.replace (frase, '.', '')
    frase = str.replace (frase, ',', '')
    frase = str.replace (frase, '!', '')
    frase = str.replace (frase, '?', '')
    lista = str.split (frase, ' ', -1)
    lista = lista[-1::-1]
    return str.join(' ',lista)