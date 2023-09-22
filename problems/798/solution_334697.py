def freq_palavras(frases):
    '''funcao que recebe uma string e retorna um dicionario
    onde cada palavra dessa string seja uma chave e tenha como
    valor o numero de vezes que a palavra aparece
    string->dicionario'''
    separar_palavras=str.split(frases)
    dicionario={}
    for elementos in separar_palavras:
        if list.count(separar_palavras,elementos)==1:
            dicionario[elementos]= 1
        if list.count(separar_palavras,elementos)>1:
            dicionario[elementos]= list.count(separar_palavras,elementos)
        
    return dicionario