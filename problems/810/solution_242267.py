def retira_pontuacao(frase):
    '''Função que retira a potuação de uma frase dada. Dentre
    os caracteres que serão removidos estão: travessão, vírgula
    dois pontos, ponto e vírgula e pontos de encerramento de
    frase
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
    if '?' in frase:
        frase = str.replace(frase, '?', ' ')
    if '!' in frase:
        frase = str.replace(frase, '!', ' ')
    
    return frase

def inverte(frase):
    '''Função que dada uma frase retorna outra frase com
    os mesmos elementos das de entrada, porém invertidos
    sem letras maíusculas e sem pontuação
    str -> str'''
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    palavras_frase = str.split(frase)
    list.reverse(palavras_frase)
    frase_final = str.join(' ', palavras_frase)
    
    return frase_final