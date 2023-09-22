def freq_palavras(frases):
    '''retorna um dicionário com cada palavra da frase e o número de vezes que ela aparece;
    str->dict'''
    
    palavras=str.split(frases,' ')
    dicionario={}
    
    for i in palavras:
        if i not in dict.keys(dicionario):
            dicionario=dicionario + i
            dicionario[i]=1
        
        else:
            dicionario[i]=dicionario[i]+1
            
    return dicionario