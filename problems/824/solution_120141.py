def	uppCons (frase):
    ''' Função que retorna todas as suas consoantes em letras maiusculas. str->str'''
    frasenova=''
    i=0
    while i<len(frase):
        if str.lower(frase[i]) in 'bcçdfghjklmnpqrstvwxz':
            frasenova=frasenova + frase[i]
            i=i+1
        else:
            frasenova=frasenova + frase[i]
            i=i+1
    return frasenova