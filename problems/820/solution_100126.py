def posLetra(string,letra,n):  
    """
    Função que recebe uma frase, uma letra e um número. Com isso, retornamos a posição da 
    frase que aquela ocorrência da letra está.
    str, str, int -> int
    """
    def posLetra(string,letra,n):
        i=0
        indice=0
        while i<len(string):
            x=str.find(string,letra)
            indice=indice+x
            i=i+0
        return indice