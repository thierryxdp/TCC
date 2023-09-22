def retira_pontuacao(frase):
    " " "Retorna a frase onde todos os caracteres de pontuação são substituidos por espaço;str, -> str " " "
    frase = str.replace(frase,'...','.')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    return frase