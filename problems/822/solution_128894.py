def repetidos(lista):
    '''função que dado um lista retorne o número de vezes que
    um elemento da lista é igual ao elemento anterior'''
    repeticao=0
    proximo=0
    while proximo<len(lista):
    	if lista[proximo]==lista[proximo+1]:
          	repeticao=repeticao+1
       	proximo= proximo +1
    return repeticao