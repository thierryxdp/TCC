def posLetra(string,letra,pos):
    '''
    Recebe uma string, uma string consistindo em apenas uma letra e um inteiro pos 
    e retorna um inteiro com a posição da pos ocorrência de letra na string
    
    str, str, int -> int
    '''
    i=-1
    j=0
    while j<pos and pos<=str.count(string,letra):
    	if string[i+1]==letra:
        	j=j+1
        i=i+1
    return i