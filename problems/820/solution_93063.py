def posLetra(string,letra,ocorrencia):
    """retorna em que posição da string a
ocorrencia da letra está
ex: posLetra('Leonardo lindo','l',2)
--- 9"""
    i = 0
    novalista = [] #criando uma lista nova
    
    if str.find(string,letra) == -1:  #verifica se há letra na string, primeiro caso
        return -1

    while i < len(string):
        
        if str.find(string[i:i+1],letra) != -1:
            
            novalista = novalista + [str.index(string,letra,i)]
            
        i = i + 1

    
    if ocorrencia <= len(novalista): #verificando se a ocorrencia ultrapassa o limite das letras
        return novalista[ocorrencia-1] #o '-1' para voltar a opção anterior, ja que por exmeplo a primeira posicao é 0
    else:
        return -1