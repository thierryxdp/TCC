def inverte(x):
    s1=str.replace(x,'!',' ')
    s2=str.replace(s1,':',' ')
    s3=str.replace(s2,';',' ')
    s4=str.replace(s3,'?',' ')
    s5=str.replace(s4,'-',' ')
    s6=str.replace(s5,'.',' ')
    s7=str.replace(s6,',',' ')
    
    frase=str.split(s7)
    list.reverse(frase)
    frase=str.join(' ', frase)
    return str.lower(frase)