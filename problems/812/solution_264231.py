def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase onde todos os caracteres de pontuação são substituídos por espaço'''
    if '-' in frase:
        return str.join(" ",str.split((frase),'-'))
    else:
        return str.join(" ",str.split((frase),','))
    else:
        return str.join(" ",str.split((frase),':'))
    else:
        return str.join(" ",str.split((frase),';'))
    else:
        return str.join(" ",str.split((frase),'.'))