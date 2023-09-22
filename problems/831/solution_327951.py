#Entrada:A função recebe uma palavra
#1 - Tranformar a palavra em uma lista
#2 - Precisamos percorrer toda  lista palavra em busca de uma vogal
#3 - Ao encontarmos, adicionamos um 'p' após a vogal, mais a vogal orginal
#4 - Retornar a palavra, após converter a lista e, uma string
def lingua_p(palavra: str) -> str:
    """Recebe uma palavra e retorna a mesma mas adicionando
    um 'p' após cada vogal mais a respectiva vogal"""
    listaPalavra=list(palavra)
    listaAux=[]
    i=0
    for letra in listaPalavra:
        if letra.lower() in 'aeiouéáóúàãõ':
            listaAux.append(letra)
            listaAux.append('p')
            listaAux.append(letra)
        	#listaPalavra.insert(i+1, 'p')
        else:
            listaAux.append(letra)
        i+=1
    return str.join('',listaAux)