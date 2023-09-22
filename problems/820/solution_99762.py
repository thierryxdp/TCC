def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
	i=0
    qtd=0
    while i<len(frase):
        if frase[i]==letra:
            qtd+=1
            if qtd==ocorrencia:
                return i
            i+=1