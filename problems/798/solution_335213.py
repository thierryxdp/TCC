def freq_palavras(frases):
    '''A função recebe uma string como chave e retorna um dicionario
    que tenha como valor o numero de vezes que a string aparece.
    str->dict'''
    
    palavras=str.split(frases)
    dic={}
        
    for palavra in palavras:
        if palavra not in dic:
            dic[palavra]=1
        else:
            dic[palavra]=dic.get(palavra)+1
    return dic