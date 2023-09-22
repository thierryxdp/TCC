def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário onde cada
    palavra da string é uma chave e o valor é o número de vezes em que
    a palavra aparece
    str->dict'''
    
    x=frases.split(' ')
    dicio={}
    
    for palavras in x:
        dicio=[palavras]
        y=x.count(palavras)
        
      
        
    return dicio,y