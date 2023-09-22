def retira_pontuacao(texto):
    '''funcao que retira os elementos de um texto(travessao,vırgula,dois pontos,ponto e vırgula,ponto final,ponto de exclamacao e ponto de interroragacao)
    str->str'''
    return str.lower(texto).replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' ')
    
def inverte(texto):
    '''funcao que dado um texto inverte este texto,sem letras maisculas e retirando toda sua pontuacao
    str->str'''
    frase = str.split(retira_pontuacao(texto))
    list.reverse(frase)
    return str.join(' ',frase)