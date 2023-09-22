def retira_pontuacao(f):
    f=str.replace(f,'...',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'-',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,':',' ')
    f=str.replace(f,'!',' ')
    
    return f
def inverte_(frase):
    frase= retira_pontuacao(frase)
    frase=str.lower(frase)
    lista=str.split(frase,' ')
    lista[::-1]
    
    return str.join(' ',lista[::-1])