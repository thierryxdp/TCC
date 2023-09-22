def posLetra(frase,letra,ocorrencia):
    """Recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra e retorna
    em que posição da string aquela ocorrência da letra está"""
    """str,str,int -> int"""
    
    i = 0
    rodou = 0
    while rodou < ocorrencia:
        if str.find(frase,letra,i) >= 0:
            str.find(frase,letra,i) = i 
            rodou = rodou + 1
           
            
    return str.find(frase,letra,i)