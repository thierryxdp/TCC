def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário onde cada palavra da string seja uma chave;
    e possua como valor o número de vezes que a palavra aparece;
    str -> dict'''
    frases = frases.split()
    dic = {}
    
    for palavra in frases:
        if palavra in dic:
            dic[palavra]+=1
        else:
            dic[palavra]=1
    return dic