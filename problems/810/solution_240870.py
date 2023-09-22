def inverte(frase):
    '''inverte as palavras do texto retirando a pontuacao str->str'''
    s_pontuacao=frase
    s_pontuacao=s_pontuacao.replace('.',' ')
    s_pontuacao=s_pontuacao.replace('...',' ')
    s_pontuacao=s_pontuacao.replace(',',' ')
    s_pontuacao=s_pontuacao.replace('!',' ')
    s_pontuacao=s_pontuacao.replace('?',' ')
    s_pontuacao=s_pontuacao.replace('-',' ')
    lista_s_ponto =s_pontuacao.split(' ')
    lista_invertida=lista_s_ponto[::-1]
    
    return str.join('',lista_invertida)