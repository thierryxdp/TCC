def freq_palavras(x):
    'Função que recebe uma frase e retorna as palavras que a compõem e o número de vezes que essas palavras aparecem.'
    'str->dict'
    frase=str.split(x)
    dici={}
    for palavra in frase:
        dici[palavra]=list.count(frase,palavra)
        
    return dici