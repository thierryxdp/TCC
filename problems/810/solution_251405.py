def retira_pontuacao(f):
    ''' retorna uma frase que qualquer caractere de pontuação tenha sido substituído por espaço;
    str -> str ''' 
    t = str.replace(f,'-',' ')
    v = str.replace(t,',',' ')
    d_ps = str.replace(v,':',' ')
    pvc = str.replace(d_ps,';',' ')
    p = str.replace(pvc,'.',' ')
    e = str.replace(p,'?',' ')
    i = str.replace(e,'!',' ')
    r = str.replace(i,'...',' ')
    return r
def inverte(f):
    ''' retorna uma frase que contenha as mesmas palavras de f na ordem inversa, sem letras maiúsculas, e sem a pontuação;
    str -> str '''
    r = retira_pontuacao(f)
    m = str.lower(r)
    s = str.split(m)
    lista.reverse(s)
    return str.join('',s)