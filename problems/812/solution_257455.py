def retira_pontuacao(frase):
    '''funcao q substitui caracteres de pontuacao da frase como:
    virgulas,ponto,travessao,ponto e virgula,dois pontos e pontuacao
    de encerramento de frase por espaco'''
    a=str.replace(frase,',',' ')
    b=str.replace(a,'.',' ')
    c=str.replace(b,'-',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,':',' ')
    f=str.replace(e,'!',' ')
    g=str.replace(f,'?',' ')
    return g