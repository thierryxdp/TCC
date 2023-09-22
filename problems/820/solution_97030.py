def posLetra(texto,letra,ocorrencia):
    '''Função que dada uma string com um texto ou frase (texto),
    uma letra (letra) e ocorrencia esperada (ocorrencia) retorna 
    o índice da ocorrencia pedida da letra no texto.
    str,str,int -> int 
    '''
    i=0
    cont_ocorrencia=0 #funciona como um contador de ocorrência 
    
    while i< len(texto):
        if texto[i]==letra:
            cont_ocorrencia=cont_ocorrencia+1
            if cont_ocorrencia == ocorrencia:
                return i
                
        i=i+1
        
    return -1