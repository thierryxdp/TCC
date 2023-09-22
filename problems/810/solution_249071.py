def inverte(texto):
    '''funcao que retira os elementos de um texto(travessao,vırgula,dois pontos,ponto e vırgula,ponto final,ponto de exclamacao e ponto de interroragacao)
    str->str'''
    str.lower(texto).replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' ')
    list.reverse(texto)
    return str.join('',texto)