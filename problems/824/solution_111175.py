def uppCons(f):
    ''' Função que resebe uma frase f e retorna a propria com suas consoantes em maiúsculo.
    str->str'''
    i=0
    j=list(f)
    s=len(j)
    while(i<s):
        if ( (j[i]!='a') and (j[i]!='ã') and (j[i]!='á') and (j[i]!='â') and (j[i]!='à') and (j[i]!='e') and (j[i]!='é') and (j[i]!='è') and (j[i]!='ê') and (j[i]!='i') and (j[i]!='í') and (j[i]!='ì') and (j[i]!='î') and (j[i]!='o') and (j[i]!='õ') and (j[i]!='ó') and (j[i]!='ò') and (j[i]!='ó') and (j[i]!='u') and (j[i]!='ú') and (j[i]!='û') and (j[i]!='ù')):
            j[i]= str.upper(j[i])
        i=i+1
    return str.join('',j)