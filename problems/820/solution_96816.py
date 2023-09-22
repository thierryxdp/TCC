def posLetra(texto,letra,ocorrencia):
    '''Função que dada uma string com um texto ou frase (texto),
    uma letra (letra) e ocorrencia esperada (ocorrencia) retorna 
    o índice da ocorrencia pedida da letra no texto.
    str,str,int -> int 
    '''
    i=0
    x=0
    while i< len(texto):
        if texto[i]==letra:
            x=x+1
            if x== ocorrencia:
                return i
                
        i=i+1
        
    return -1