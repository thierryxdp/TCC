def posLetra(frase,l,oc):
    '''Dada uma string,uma letra e um número que indica posição, retorna qual a posição que aquela ocorrencia da letra corresponde
    str,str,int->int'''
    vezes=0
    i=0    
    while i< len(frase):
        if oc==0:
            return -1
        
        if frase[i]==l:
            vezes=vezes+1
            
        if vezes==oc:
            return i
    i=i+1
         else:
            return -1