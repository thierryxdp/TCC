def retira_pontuacao(frase):
    '''Frase que dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço'''
    ',' and '.' in frase='a'
    '-' and '!' in frase='b'
    '-' and '.' in frase='c'
    if 'a' in frase:
        return str.join(" ",str.split((frase),'a'))
    if 'b' in frase:
        return str.join(" ",str.split((frase),'b'))
    if 'c' in frase:
        return str.join(" ",str.split((frase),'c'))
    if '?' in frase:
        return str.join(" ",str.split((frase),'?'))
    if '!' in frase:
        return str.join(" ",str.split((frase),'!'))
    if ':' in frase:
        return str.join(" ",str.split((frase),':'))
    if ';' in frase:
        return str.join(" ",str.split((frase),';'))
    if '.' in frase:
        return str.join(" ",str.split((frase),'.'))