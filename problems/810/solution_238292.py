def retira_pontuacao(frase):
    '''A função vai retirar todos os tipos de pontuação de uma frase inserida pelo usuário.
    
    dados de entrada -> string
    dados de saída -> string'''
        
    x = str.count(frase, "-")
    y = str.count(frase, ",")
    z = str.count(frase, ":")
    i = str.count(frase, ";")
    i = str.count(frase, ".")
    j = str.count(frase, "!")
    k = str.count(frase, "?")
        
    if x != 0 or y != 0 or z != 0 or i != 0 or j != 0 or k != 0:
    	x1 = str.replace(frase,"-"," ")
        x2 = str.replace(x1,","," ")
        x3 = str.replace(x2,":"," ")
        x4 = str.replace(x3,";"," ")
        x5 = str.replace(x4,"."," ")
        x6 = str.replace(x5,"!"," ")
        final = str.replace(x6,"?"," ")
            
        return final
        
	else:
    	return frase
    
def inverte(frase):
	'''A função vai inverter a ordem das palavras de uma frase
        
    dados de entrada -> string
    dados de saída -> string'''
        
    x = retira_pontuacao(frase)
    lista = str.split(x," ") #separando as palavras da string em uma lista
    Q = len(lista) #Quantidade de palavras que existem na lista
        
    juncao = str.join(" ",lista[0:-Q:1])
        
    return juncao