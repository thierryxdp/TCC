def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra é uma chave e o número
    de vezes que aparece é o seu valor
    assinatura: string --> dic
    """
    lista=frases.split(' ')
    dic= {lista[0] : frases.count(lista[0])}
    for i in range(1,len(lista)):
    	dic.update({lista[i] : frases.count(lista[i])})
         	  
    return dic