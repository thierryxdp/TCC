def retira_pontuacao(frase):
    '''Função que dada uma frase, a retorna com caracteres de pontuação substituídos por espaço; str -> str'''
    return str.replace(frase,'-',' ' ) and str.replace(frase,',',' ') and str.replace(frase,':',' ' ) and str.replace(frase,';',' ' )