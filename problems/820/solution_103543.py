def posLetra(frase, letra, num):

    i = 0
   
    if str.count(frase,letra) < (num):
        return -1
        
    while i < len(frase):
        return str.find(frase,letra,num-1)
        i += 1