def conta_frases(frase):
    s=frase
    f1=len(s.replace('.',''))-1
    f2=len(s.replace('?'))-1
    f3=len(s.replace('...'))-1
    f4=len(s.replace('!'))-1
   	
    return f1+f2+f3+f4