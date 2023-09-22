def retira_pontuacao(frase):
    '''A funcao retira todas pontuacoes e retorna 
       em seu lugar um espaço;
       str -> str'''
    pontuacao = ['?', ',','!''.']
    passo1_pnt=str.replace(frase,pontuacao,' ')
    passo2_exc=str.replace(passo1_pnt,'!',' ')
    passo3_vir=str.replace(passo2_exc,',',' ')
    passo4_tra=str.replace(passo3_vir,'-',' ')
    passo5_int=str.replace(passo4_tra,'?',' ')
    return passo5_int