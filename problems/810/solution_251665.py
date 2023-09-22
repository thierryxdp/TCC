def inverte(frase):
    '''retorna uma nova frase na forma inversa da frase original, sem letra maiúscula e sem pontuação;
    str->str'''
    maiusc=str.lower(frase)
    f1=str.replace(maiusc,',','')
    f2=str.replace(f1,'-',' ')
    f3=str.replace(f2,':','')
    f4=str.replace(f3,'...','')
    f5=str.replace(f4,'.','')
    f6=str.replace(f5,'!','')
    f7=str.replace(f6,'?','')
    f8=str.replace(f7,';','')
    listafrase=str.split(f8)
    listainvert=listafrase[-1:0]
    
    return listainvert