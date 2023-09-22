def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra é uma chave e o número
    de vezes que aparece é o seu valor
    assinatura: string --> dic
    """
    lista=frases.split(' ')
    dic={}
    for i in range(0, len(lista)):
                  dic=({lista[i] : frases.count(lista[i])})
            	  
    return dic