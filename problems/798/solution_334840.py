def freq_palavras(frases):
2	    lista = str.split(frases)
3	    dic = []
4	    for n in lista:
5	        qtd = list.count(lista, n)
6	        list.append(dic,{n: qtd})
7	    return dic