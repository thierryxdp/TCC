def freq_palavras(frases): 
    frases = str.split()          
    str2 = [] 
    for i in frases:              
        if i not in str2: 
            str2.append(i) 
        for i in range(0, len(str2)): 
            return( str2[i], str.count(str2[i]))