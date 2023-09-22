def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i]=='b':
            con = con + frase.replace(frase[i],'B')
        if frase[i]=='c':
            con = con + frase.replace(frase[i],'C')
        if frase[i]=='d':
            con = con + frase.replace(frase[i],'D')
        if frase[i]=='f':
            con = con + frase.replace(frase[i],'F')
        if frase[i]=='g':
            con = con + frase.replace(frase[i],'G')
        if frase[i]=='h':
            con = con + frase.replace(frase[i],'H')    
        if frase[i]=='j':
            con = con + frase.replace(frase[i],'J')   
        if frase[i]=='k':
            con = con + frase.replace(frase[i],'K')
        if frase[i]=='l':
            con = con + frase.replace(frase[i],'L')
        if frase[i]=='m':
            con = con + frase.replace(frase[i],'M')
        if frase[i]=='n':
            con = con + frase.replace(frase[i],'N')
        if frase[i]=='p':
            con = con + frase.replace(frase[i],'P')
        if frase[i]=='q':
            con = con + frase.replace(frase[i],'Q')
        if frase[i]=='r':
            con = con + frase.replace(frase[i],'R')
        if frase[i]=='s':
            con = con + frase.replace(frase[i],'S')
        if frase[i]=='t':
            con = con + frase.replace(frase[i],'T')
        if frase[i]=='v':
            con = con + frase.replace(frase[i],'V')
        if frase[i]=='w':
            con = con + frase.replace(frase[i],'W')
        if frase[i]=='x':
            con = con + frase.replace(frase[i],'X')
        if frase[i]=='y':
            con = con + frase.replace(frase[i],'Y')
        if frase[i]=='z':
            con = con + frase.replace(frase[i],'Z')
    	i+=1
    
    return con