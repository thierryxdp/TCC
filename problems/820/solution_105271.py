def posLetra(frase,letra,ocorrencia):
    while 1==1:
        Letra_ind=0
        letra_ind=frase.find(letra,Letra_ind,len(frase))
        if letra_ind==-1 or frase.count(letra,0,Letra_ind+1)==ocorrencia:
        	break
   	return Letra_ind