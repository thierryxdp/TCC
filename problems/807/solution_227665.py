def conta_frases(frases):
    ''' função que conta quantas frases tem num texto
    str-> int'''
    #primeiro retirar os espaços
    # retira !,?,.,... nessa ordem
    # depois transforma em elementos diferentes cada partezinha
    # conta total de elementos
	return len(str.split(str.replace(str.replace(str.replace(str.replace(str.replace('alex.feijao!macarrao?entao ta...',' ',''),'!',' '),'?',' '),'.',' '),'...',' ')))