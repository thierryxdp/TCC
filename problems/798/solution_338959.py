def freq_palavras(frases):
    lista=frases.split(' ')
    dic= {lista[0] : lista.count(lista[0])}
    for i in range(1, len(lista)):
    	dic.update({lista[i] : lista.count(lista[i])})
         	  
    return dic