def fred_palavras(frases):
    
    words= frases.split()
    dicio= {}
    index= 0
    
    for letters in words:
        
        dicio[words[index]]= words.count(words[index])
        index +=1
        
    return dicio