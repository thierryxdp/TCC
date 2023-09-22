def retira_pontuacao(f):
    ''' retorna uma frase que qualquer caractere de pontuação tenha sido substituído por espaço;
    str -> str ''' 
    t = str.replace('f','-','')
    v = str.replace('t',',','')
    d_ps = str.replace('v',':','')
    pvc = str.replace('d_ps',';','')
    p = str.replace('pvc','.','')
    e = str.replace('p','?','')
    i = str.replace('e','!','')
    r = str.replace('i','...','')
    return t+v+d_ps+pvc+p+e+i+r