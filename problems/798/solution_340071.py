def freq_palavras(frase): 
  '''retorna um dicionario com as chaves e seu numero de repetições que ocorrem na frase
  str->dict'''
    
    frase = frase.split()          
    frase2 = []
    frequencia={}
  
    
    for i in frase:              
        if i not in frase2:
            frase2.append(i)
              
    for i in range(0, len(frase2)):
        frequencia[frase2[i]]=frase.count(frase2[i])
    return frequencia