def posLetra(frase,l,oc):
    '''Dada uma string,uma letra e um número que indica posição, retorna qual a posição que aquela ocorrencia da letra corresponde
    str,str,int->int'''
    vezes=0
    i=0    
    if str.count(frase,l)<oc:
            return -1   
    if str.count(frase,l)+1 ==oc:
        return oc

        while len(frase)<oc:
                  if frase[i]==l:
                    vezes=vezes+1
    return vezes