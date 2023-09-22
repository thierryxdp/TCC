def inverte(texto):
    '''funcao que retira os elementos de um texto(travessao,vırgula,dois pontos,ponto e vırgula,ponto final,ponto de exclamacao e ponto de interroragacao)
    str->str'''
    return str.lower(texto).replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' ')