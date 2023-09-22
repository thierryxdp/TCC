def conta_frases(frase):
    s=frase
    f1=len(s.replace('.',' ',))
    f2=len(s.replace('?',' ',))
    f3=len(s.replace('...',' ',))
    f4=len(s.replace('!',' ',))
   	
    return f1+f2+f3+f4