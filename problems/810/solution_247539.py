def inverte(frase):
	'''A função vai inverter a ordem das palavras de uma frase
        
    dados de entrada -> string
    dados de saída -> string'''
        
    x = (frase) #retirando a pontuação da string
    lista = str.split(x," ") #separando as palavras da string em uma lista
    Q = len(lista) #Quantidade de palavras que existem na lista
        
    juncao = str.join(" ",lista[Q-1:-Q-1:-1]) #Juntou as strings da lista de ordem inversa com um espaço entre elas
    minusculo = str.lower(juncao) # colocou todas as letras da string em minúsculo
        
    return minusculo