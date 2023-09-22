def freq_palavras(frases):
    ''' Função que recebe de entrada um texto (string) e 
    retorna um dicionario relacionando cada palavra a 
    quantidade de vezes que ela aparece nesse texto, em que 
    cada palavra eh a chave e a quantidade, o valor.
    str -> dict'''
    s = str.split(frases)
    dict_ret = {}
    for palavra in s:
        dict_ret[palavra] = list.count(s,palavra)
    return dict_ret