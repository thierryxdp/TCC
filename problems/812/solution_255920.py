def retira_pontuacao(frase):
    """função que retira a pontuação de uma frase, substituindo por espaços"""
    if str.find(frase,'.')!=-1 and str.find(frase,',')==-1 and str.find(frase,'!')==-1 and str.find(frase,'?')==-1 and str.find(frase,'-')==-1:
        return str.replace(frase,'.',' ')
        
    elif str.find(frase,'.')==-1 and str.find(frase,',')==-1 and str.find(frase,'!')!=-1 and str.find(frase,'?')==-1 and str.find(frase,'-')==-1:
        return str.replace(frase,'!',' ')
    
    elif str.find(frase,'.')!=-1 and str.find(frase,',')!=-1 and str.find(frase,'!')==-1 and str.find(frase,'?')==-1 and str.find(frase,'-')==-1:
        a=str.replace(frase,'.',' ')
        b=str.replace(a,',',' ')
        return b
    
    elif str.find(frase,'.')==-1 and str.find(frase,',')!=-1 and str.find(frase,'!')==-1 and str.find(frase,'?')!=-1 and str.find(frase,'-')==-1:
        c=str.replace(frase,',',' ')
        d=str.replace(c,'?',' ')
        return d
    
    elif str.find(frase,'.')!=-1 and str.find(frase,',')!=-1 and str.find(frase,'-')!=-1 and str.find(frase,'!')==-1 and str.find(frase,'?')==-1:
        e=str.replace(frase,'.',' ')
        f=str.replace(e,',',' ')
        g=str.replace(f,'-',' ')
        return g
    
    elif str.find(frase,'.')==-1 and str.find(frase,',')==-1 and str.find(frase,'-')==-1 and str.find(frase,'!')==-1 and str.find(frase,'?')!=-1:
        h=str.replace(frase,'?',' ')
        return h
    
    elif str.find(frase,'.')==-1 and str.find(frase,',')==-1 and str.find(frase,'-')!=-1 and str.find(frase,'!')!=-1 and str.find(frase,'?')==-1:    
        i=str.replace(frase,'!',' ')
        j=str.replace(i,'-',' ')
        return j