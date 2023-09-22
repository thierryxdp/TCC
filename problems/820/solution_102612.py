def posLetra(frase, letra, numero):
    '''
    função que dada uma frase, procura o índice no qual ocorre a ocorrencia desejada na letra procurada
    str,str,int--> int
    '''
    
    resposta = str.find(frase,letra)

    while resposta >= 0 and numero>1:
        resposta = str.find(frase,letra, resposta + 1)
        numero = numero - 1
        
    return resposta