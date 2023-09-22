def retira_pontuacao(frase):
    '''Função que, dada uma frase como entrada, susbtitui todos os caracteres de pontuação por espaços em branco;
    str->str'''
    
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'?',' ')