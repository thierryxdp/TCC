def posLetra(frase,l,n):
    '''Recebe como entrada uma frase,uma letra e um número indicando a ocorrencia
    e a função retorna a posição da string aquela ocorrencia da letra esta.
    str,str,int->int'''
    
    indice=1
    pos=0
    
    while indice<len(frase):
        pos = str.find(frase,l,n,-9)
        
        indice=indice+1        
    return pos