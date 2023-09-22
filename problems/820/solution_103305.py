def posLetra(frase,l,oc):
    '''Dada uma string,uma letra e um número que indica posição, retorna qual a posição que aquela ocorrencia da letra corresponde
    str,str,int->int'''
    ocorencia=0
    resto=0
    i=0    
    if str.count(frase,l)<oc:
            return -1  

    while len(frase)<i:
        if frase[i]==l:
            vezes=vezes+1
        i=i+1
          
    return i