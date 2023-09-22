def retira_pontuacao(x):
    ''' Funçao que, dada uma frase comum, retorna uma nova frase composta pelas mesmas palavras, substituindo as pontuaçoes por espaços;
    str -> str ''' 
    h = str.replace(x,'-',' ')
    v = str.replace(h,',',' ')
    d_ps = str.replace(v,':',' ')
    pvc = str.replace(d_ps,';',' ')
    p = str.replace(pvc,'.',' ')
    e = str.replace(p,'?',' ')
    i = str.replace(e,'!',' ')
    r = str.replace(i,'...',' ')
    return r