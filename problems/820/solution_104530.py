def posLetra(string,letra,n):
    ''' retona em qual posição da string a ocorrencia da
    	letra está'''
   i=0
        indice=0
        while i<len(string):
            x=str.find(string,letra)
            indice=indice+x
            i=i+0
        return indice