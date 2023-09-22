def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário
    onde cada palavra da string seja uma chave e tenha como
    valor o número de vezes que a palavra aparece.
    str -> dict'''
    repeticao=()
    fra=frase.split
    dicionario=[]    
    for fra in frases:
        if frases.count(fra)>0:            
            dicionario=fra+frases.count(fra)            
    return dicionario