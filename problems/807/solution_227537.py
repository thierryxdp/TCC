def conta_frases(frase):
    '''funcao que recebe uma string em forma de frases com 
    final '.','...','?','!' e retorna quantas frases tem atraves
    das funcoes 'count' e replace.
    str -> int'''
    return str.count(str.replace(frase,'...','.'),'.') + str.count(frase,'!') + str.count(frase,'?')