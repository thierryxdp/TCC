def posLetra(frase,letra,ocorrencia):
    """funçao que recebe uma frase, uma letra e um numero que indica a ocorrencia desejada da letra na frase e retorna a posiçao onde a letra esta na str, se ocorrencia < numero de ocorrencias na str retorna -1.
    entrada: str, str, int;
    saida: int."""
    
    pos=[]
    i=0
    
    while i < len(frase):
         if frase[n]== letra:
            pos.append(i)
         
         i+=1
       
    if len(pos)>=ocorrencia:
        return(pos[ocorrencia-1])
    
    else:
        return(-1)