def freq_palavras(frases):
    ''' a função recebe uma string como chave e retorna que tenha como valor
    o número de vezes que a palavra aparece str->dic'''
    
    palavras=str.split(frases)
    dic={}
    
    for palavra in palavras:
        if palavra not in dic:
            dic[palavra]=1
              else:
            dic[palavra]=dic.get(palavra)+1
            return dic