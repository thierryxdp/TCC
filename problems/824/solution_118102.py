def uppCons(x):
    """Função que retorna uma string com todas suas consonanantes em maíusculo"""
    """str--->str"""
    frase=''
    i=0
    while i<len(x):
        if x[i] in 'qwrtypsdfghjklçzxcvbnm':
            frase+=str.upper(x[i])
        else:
            frase+=x[i]
    i+=1
        return frase