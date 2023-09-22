def posLetra(palavra,letra,n):
    
   	if letra not in palavra:
        return -1
    else:
        return str.find(palavra,letra,n)