def retira_pontuacao(frase):
    '''A funcao retira todas pontuacoes e retorna 
       em seu lugar um espaço;
       str -> str'''
    passo1_pnt=str.replace(frase,'.',' ')
    passo2_exc=str.replace(passo1_pnt,'!',' ')
    passo3_vir=str.replace(passo2_exc,',',' ')
    passo4_tra=str.replace(passo3_vir,'-',' ')
    return passo4_tra