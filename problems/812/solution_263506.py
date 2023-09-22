def retira_pontuacao(frase):
    ''' função que retorna a frase substituíndo todos os sinais de pontuação por espaço
     string->string'''
    frase= str.replace(frase,'-',' ')
    frase= str.replace(frase,',',' ')
    frase= str.replace(frase,':',' ')
    frase= str.replace(frase,';',' ')
    frase= str.replace(frase,'.',' ')
    frase= str.replace(frase,'?',' ')
    frase= str.replace(frase,'!',' ')
    return frase