def posLetra(conteudo_str,letra,num_ocorrencia):
    '''
    Função que retorna a posição ,dentro da string,  da ocorrência desejada de uma letra, após receber a string
    a letra e o número de tal ocorrência.
    '''
    if str.count(conteudo_str,letra)<num_ocorrencia:
        return -1
    
    letras=()
    contador=0
    
    while proximo<len(conteudo_str):
        if conteudo_str[contador]==l:
            letras=letras+(contador,)
        contador=contador+1
        
    return indices[num_ocorrencia-1]