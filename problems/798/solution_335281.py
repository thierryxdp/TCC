def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário
    onde cada palavra da string seja uma chave e tenha como
    valor o número de vezes que a palavra aparece.
    str -> dict'''    
    fra=fra.split()
    dicionario=[]    
    for palavra in fra:
        dicionario(palavra)=list.count(frases,palavra)          
    return dicionario