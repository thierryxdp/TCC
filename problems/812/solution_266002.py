def retira_pontuacao(f):
    ''' retorna uma frase que qualquer caractere de pontuação tenha sido substituído por espaço;
    str -> str ''' 
    t = str.replace('f','-','')
    v = str.replace('f',',','')
    d_ps = str.replace('f',':','')
    pvc = str.replace('f',';','')
    p = str.replace('f','.','')
    return p