def freq_palavras(frases):
    "recebe uma string e retorna um dicionario onde cada palavra dessa string é uma chave e o valor é o número de vezes que tal palavra aparece"
    lista = [str.split(frases,' ')]
    listanova = []
    dicionario = {}
    for elemento in lista:
        while list.count(listanova,elemento) <1:
            listinha = [elemento,list.count(lista,elemento)]
            list.append(listanova,listinha)
    return listanova
    for listinha in listanova:
            dicionario[listinha[0]]=listinha[1]
    return dicionario