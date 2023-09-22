def posLetra(frase, letra, num):

    i = 0
   
    if str.count(frase,letra) > (num):
        while i < len(frase):
            quant = str.find(frase,letra,num-1)
            i += 1
        
        return quant

    else:
        return -1