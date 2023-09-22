def retira_pontuacao(frase):
    '''funcao que retorna uma nova frase substituindo todos os caracteres de pontuacao por uma espaço. str->str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'"',' ')
    frase=str.replace(frase,',',' ')
    
    return frase