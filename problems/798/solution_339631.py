def freq_palavras(frases):
    '''função que recebe uma string e retorne um dicionário onde cada palavra da string
seja uma chave e tenha como valor o número de vezes que ela aparece
string->dict'''
    dic={}
    palavras=frases.split(' ')
    for string in palavras:
        indice=palavras.count(string)
        dic[string]=indice
    return dic