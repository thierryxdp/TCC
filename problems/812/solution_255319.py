def retira_pontuacao(frase):
    '''Função que dada uma frase com as seguintes pontuações !, ?, ., ',' , :, ; e -
    substitui cada uma por espaço(' ') e escreve a frase retornada sem esses caracteres
    str->str'''
    frase0=frase
    frase1=str.replace(frase0,'.',' ')
    frase2=str.replace(frase1,'-',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,';',' ')
    frase5=str.replace(frase4,',',' ')
    frase6=str.replace(frase5,'?',' ')
    frase7=str.replace(frase6,'!',' ')
    return frase7