def conta_frases(frase):
    s=frase
    f=len(s.replace('.',' ',))
    f=len(f.replace('?',' ',))
    f=len(f.replace('...',' ',))
    f=len(f.replace('!',' ',))
   	
    return f