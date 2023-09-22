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
    lista_min=lista_invertida.lower
    lista_s_espaco=lista_min.strip
    return str.join(' ',lista_s_espaco)