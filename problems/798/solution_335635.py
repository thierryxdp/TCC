def freq_palavras(frases):
    '''funcao que dada uma string contendo frases, retorna um dicionario onde cada palavra dessa string e uma chave e a quantidade de vezes que ela se repete, o valor;
       str->dict'''
    dicionariofinal={}
    palavrastotal= str.split(frases)
    for palavra in palavrastotal:
        dicionariofinal[palavra]=str.count(frases, palavra)
    return dicionariofinal