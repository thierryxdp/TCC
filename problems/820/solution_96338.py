def posLetra(string,x, y):
    contador = 0
    aparicao = 0
    while contador < len(string):
        for i in string:
            if i == x:
                aparicao = aparicao +1
            	if aparicao == y:
                	contador = contador + 1
        if aparicao <= y:
            return -1