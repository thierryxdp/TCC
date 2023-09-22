def freq_palavras(frases):
    "recebe uma string e retorna um dicionario onde cada palavra dessa string é uma chave e o valor é o número de vezes que tal palavra aparece"
    lista = [str.split(frase,' ')]
    listanova = []
    dicionario = {}
    for elemento in lista:
        if not elemento in listanova:
            list.append(listanova,[elemento,list.count(lista,elemento)])
    for elemento in listanova:
        dicionario[elemento[0]]=elemento[1]
    return dicionario