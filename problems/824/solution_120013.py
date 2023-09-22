def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i]=='b':
            con = frase.replace(frase[i],'B')
        if frase[i]=='c':
            con = frase.replace(frase[i],'C')
        if frase[i]=='d':
            con = frase.replace(frase[i],'D')
        if frase[i]=='f':
            con = frase.replace(frase[i],'F')
        if frase[i]=='g':
            con = frase.replace(frase[i],'G')
        if frase[i]=='h':
            con = con + frase.replace(frase[i],'H')    
        if frase[i]=='j':
            con = frase.replace(frase[i],'J')   
        if frase[i]=='k':
            con = frase.replace(frase[i],'K')
        if frase[i]=='l':
            con = frase.replace(frase[i],'L')
        if frase[i]=='m':
            con = con + frase.replace(frase[i],'M')
        if frase[i]=='n':
            con = frase.replace(frase[i],'N')
        if frase[i]=='p':
            con = frase.replace(frase[i],'P')
        if frase[i]=='q':
            con = frase.replace(frase[i],'Q')
        if frase[i]=='r':
            con = frase.replace(frase[i],'R')
        if frase[i]=='s':
            con = frase.replace(frase[i],'S')
        if frase[i]=='t':
            con = frase.replace(frase[i],'T')
        if frase[i]=='v':
            con = frase.replace(frase[i],'V')
        if frase[i]=='w':
            con = frase.replace(frase[i],'W')
        if frase[i]=='x':
            con = frase.replace(frase[i],'X')
        if frase[i]=='y':
            con = frase.replace(frase[i],'Y')
        if frase[i]=='z':
            con = frase.replace(frase[i],'Z')
    	
        i+=1
    
    return con