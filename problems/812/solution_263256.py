def retira_pontuacao(txt):
    """ fornecida uma frase a função retornara uma frase onde
    os caracteres de pontuação serao substituidos por espaço"""
    ntxt=txt.replace('-',' ') + txt.replace('.',' ') + txt.replace(',',' ')
    return(ntxt)