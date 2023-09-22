def retira_pontuacao(texto):
    '''Função que retorna a frase onde todos os caracteres de 
    pontuação tenham sido substituídos por espaço.
    texto=str->str'''
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,',',' ')
    texto=str.replace(texto,':',' ')
    texto=str.replace(texto,';',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,'...',' ')
    texto=str.replace(texto,'.',' ')
    return texto