def lingua_p(palavra):
    '''funcao que recebe como parametro uma palavra em portugues e retornaa mesma palavra
    traduzida para a lingua do P, str->str'''
    traducao=""
    palavra=str.lower(palavra)
    restricao='qwrtyopsdfghjklçzxcvbnm'
    for i in range(len(palavra)):
    	if palavra[i] not in restricao:
    		traducao+=palavra[i]+'p'+palavra[i]
    else:
        	traducao+=palavra[i]
        return palavra