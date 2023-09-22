def inverte(frase):
    s=frase.replace(',',' ')
    s1=s.replace('.',' ')
    s2=s1.replace(';',' ')
    s3=s2.replace(':',' ')
    s4=s3.replace('?', ' ')
    s5=s4.replace('!',' ')
    frase=str.lower(s5)
    separar=frase.split()
    separar.reverse()
    fn=str.join(" ", separar)
    return fn