def retira_pontuacao(texto):
    '''funcao que retira os elementos de um texto(travessao,vırgula,dois pontos,ponto e vırgula,ponto final,ponto de exclamacao e ponto de interroragacao)
    str->str'''
    return texto.replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' ')

def minusculo(texto):
    '''funcao que dado um texto coloca as letras em minusculos deste texto
    str->str'''
    return str.lower(texto)
    
def inverte(texto):
    '''funcao que dado um texto inverte este texto,sem letras maisculas e retirando toda sua pontuacao
    str->str'''
    return str.lower(list.reverse(texto))