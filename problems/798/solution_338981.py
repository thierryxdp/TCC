def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra é uma chave e o número
    de vezes que aparece é o seu valor
    assinatura: string --> dic
    """
    dic={}
    lista=frases.split(' ')
    for i in range(len(lista)):
    	dic=dic.update(lista[i] : lista.count(lista[i]))
         	  
    return dic