def retira_pontuacao(frase):
    '''Dada uma frase, retorna a mesma onde todos os caracteres de pontuacao foram substituidos por espacos.
    str -> str'''
    if '-' in frase:
        frase = str.replace(frase, '-', ' ')
    if ', ' in frase:
        frase = str.replace(frase, ', ', ' ')
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

def inverte(frase):
    '''Dado uma frase, retorna a mesma toda em minusculo e invertida.
    str -> str'''
    semPont = retira_pontuacao(frase)
    minusculo = str.lower(semPont)
    semEspaco = str.strip(minusculo)
    lista = str.split(semEspaco, ' ')
    inverte = lista[::-1]
    string = str.join(' ', inverte)
    return string