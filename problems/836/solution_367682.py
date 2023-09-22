def busca(texto,lista):
    """Dada uma lista de informacoes de contatos de funcionarios e o setor de uma empresa, retorna as informacoes de todos os contatos desse setor"""
    """entrada: lista(lista), str
    saida:lista"""
    
    lista1 = lista[:]
    
    resultado = []
    

    for pos in range(len(lista1)):
        if texto in lista1[pos][2]:
            list.append(resultado,lista[pos])
        
        pos=pos+1
        
    for pos1 in range(len(resultado)):
        if texto in resultado[pos1]:
            list.remove(resultado[pos1],texto)
            
    	pos1=pos1+1

    return resultado