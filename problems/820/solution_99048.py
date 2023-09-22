def posLetra(string,letra,numero):
    """ função que dado uma string  e uma letra e numero
    a função calcula e retorna a posição da letra na string 
    o numero significa a ocorrência= 1 é a prmeira vez que ela aparece
    2 segunda vez ...
    caso exita menos ocorrência da letra do que a ocorrência pedida a função retorna -1
    caso seja maior ou igual ela retorna o indice que se encontra ela
    
    entrada-> str,str, int
    retorna-> str"""
    
    repeticoes=0
    
    qtd_ocorren= str.count(string,letra)
    indice=0
    
    if numero> qtd_ocorren:
        return -1
    
    else:
        while repeticoes< numero:
            indice= indice+ str.find(string,letra)  
            repeticoes= repeticoes +1
        
    return indice