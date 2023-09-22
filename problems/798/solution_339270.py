def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário onde cada
    palavra da string é uma chave e o valor é o número de vezes em que
    a palavra aparece
    str->dict'''
    
    x=frases.split(' ')
    dicio={}
    
    for i in frases:
        dicio=dicio+dict(x)
      
        
    return dicio