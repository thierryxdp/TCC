def inverte(frase):
	'''A função vai inverter a ordem das palavras de uma frase
        
    dados de entrada -> string
    dados de saída -> string'''
        
    x = retira_pontuacao(frase)
    lista = str.split(x," ")
    Q = len(lista)
        
    juncao = str.join(" ",lista[Q-1:-Q-1:-1])
    minusculo = str.lower(juncao)
        
    return minusculo