def freq_palavras(frases):
    '''
       Função que retorna um dicionário com as palavras no lugar das chaves
       e a qtd de vezes q ela aparece, no lugar do valor da chave
       list->dicio
    '''
   
    dicio={}
    frase2=frases.split()
    
    for i in frase2:
         dicio[frase2[i]]=frase2.count(frase2[i])
            
         i+=1
    
    return dicio