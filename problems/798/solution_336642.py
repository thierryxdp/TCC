def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário onde cada palavra da string seja uma chave;
    e possua como valor o número de vezes que a palavra aparece;
    str -> dict'''
    frases = frases.split()
    dic = {}
    i =1
    
    for palavra in frases:
        if palavra not in dic:
            dic= dic, {palavra:i}
        else:
            dic= dic, {palavra:i}
            i+=1
    return dic