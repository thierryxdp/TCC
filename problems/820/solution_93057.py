def posLetra(frase,letra,ocorrência):
    """Dado uma frase, uma letra e um número que representa a ocorrência desejada da letra; a função retorna a posição que represente onde tal ocorrência da letra está;
    str,str,int->int"""
    indice=0
    repetições=1
    while repetições!=ocorrência+1:
        posição=str.index(frase,letra,indice)
        indice=posição+1
        repetições=repetições+1
        
    return posição