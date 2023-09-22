def retira_pontuacao(frase):
    '''Função que dada uma frase, a retorna com caracteres de pontuação substituídos por espaço; s0tr -> str'''
    frase1 = str.replace(frase,'-',' ' )
    frase2 = str.replace(frase1,',',' ') 
    frase3 = str.replace(frase2,':',' ' ) 
    frase4 = str.replace(frase3,';',' ' )
    return frase4