def posLetra(frase,letra,numero):
	'''Retorna a posição da letra em função do número
    de ocorrências; recebe como parâmetro uma frase
    acompanhada de uma letra e o numero de ocorrencias
    que essa letra aparece na frase;String,String,int
    -->Int'''
    i=0
    pos=0
    ocorre=str.count(frase,letra)
    if ocorre<numero:
        return -1
    else:
        while i<len(frase) and ocorre!=0:
            if(frase[i]==letra):
                pos=i
                ocorre-=1
            i=i+1
        return pos