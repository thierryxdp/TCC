def posLetra(string,letra,num):
    """Funçao que recebe uma string, uma letra e um número e retorna em que posiçao da string aquela ocorrencia
    da letra está. Se existir menos ocorrencias da letra do que a pedida deve retornar -1"""
    
    lista = list(string)
    
    if lista.count(letra) >= num:
        
        contagem = 0
        proximo = 0
        
        while (contagem != num):
            
            if lista[proximo] == letra:
                
                contagem = contagem + 1
            proximo = proximo + 1
            
        return proximo - 1
    
    else:
        
        return -1