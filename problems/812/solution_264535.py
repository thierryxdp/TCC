def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase onde todos os caracters de pontuação tenham sido substituídos por espaço'''
    if '-' and '.' in frase:
        return str.join(" ",str.split((frase),'-')) and str.join(" ",str.split((frase),'.'))
    if ','and '.' in frase:
        return str.join(" ",str.split((frase),',')) and str.join(" ",str.split((frase),'.'))
    if ':' and '.' in frase:
        return str.join(" ",str.split((frase),':')) and str.join(" ",str.split((frase),'.'))
    if ';' and '.' in frase:
        return str.join(" ",str.split((frase),';')) and str.join(" ",str.split((frase),'.'))
    if '?' in frase:
        return str.join(" ",str.split((frase),'?'))
    if '!' in frase:
        return str.join(" ",str.split((frase),'!'))