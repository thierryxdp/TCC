def retira_pontuacao(frase):
    '''Frase que dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço'''
 
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