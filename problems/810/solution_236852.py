def retira_pontuacao(frase):
    '''Dada uma frase, retorna a mesma onde todos os caracteres de pontuacao foram substituidos por espacos.
    str -> str'''
    if '-' in frase:
        frase = str.replace(frase, '-', ' ')
    if ',' in frase:
        frase = str.replace(frase, ',', ' ')
    if ':' in frase:
        frase = str.replace(frase, ':', ' ')
    if ';' in frase:
        frase = str.replace(frase, ';', ' ')
    if '.' in frase:
        frase = str.replace(frase, '.', ' ')
    if '!' in frase:
        frase = str.replace(frase, '!', ' ')
    if '?' in frase:
        frase = str.replace(frase, '?', ' ')
    return frase

def inverte(texto):
    '''Dado uma frase, retorna a mesma toda em minusculo e invertida.
    str -> str'''
    semPont = retira_pontuacao(texto)
    minusculo = str.lower(semPont)
    lista = str.split(minusculo, ' ')
    string = str.join(' ', lista)
    return string