def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionário onde
    cada palavra dessa string é uma chave e tenha como valor
    o número de vezes que a palavra aparece.
    string -> dici'''
    l_frases = frases.split()
    dici = {}
    for i in l_frases:
        cont = l_frases.count(i)
        dici[i] = cont
    print(dici)