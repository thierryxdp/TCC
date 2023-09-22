def	uppCons (frase):
    ''' Função que retorna todas as suas consoantes em letras maiusculas. str->str'''
    frasenova=''
    i=0
    while i<len(frase):
        if str.lower(frase[i]) in 'bcçdfghjklmnpqrstvwxz':
            list.append(frasenova,str.upper(frase[i]))
            i=i+1
    return frasenova