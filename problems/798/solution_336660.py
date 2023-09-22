def freq_palavras(frases):
    '''recebe uma string (frases) e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavras aparece. str -> dict'''

    dic = {}
    
    lista_palavras = str.split(frases," ")
    
    cont = 0
    
    for i in range(0,len(lista_palavras)):        
        for x in range(0,len(lista_palavras)):
            if lista_palavras[i] == lista_palavras[x]:
                cont = cont + 1

        dic[lista_palavras[i]] = cont
        cont = 0
                
    return dic