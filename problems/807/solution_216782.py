def conta_frases(frase):
    s=frase
    f1=len(s.split('.'))-1
    f2=len(s.split('?'))-1
    f3=len(s.split('...'))-1
    f4=len(s.split('!'))-1
   	
    return f1+f2+f3+f4