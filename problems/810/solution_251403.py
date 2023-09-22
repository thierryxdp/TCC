def inverte(f):
    ''' retorna uma frase que contenha as mesmas palavras de f na ordem inversa, sem letras maiúsculas, e sem a pontuação;
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