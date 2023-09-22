def posLetra(s,l,num):
    """Função que recebe uma string, uma letra e um numero, que indica a ocorrencia
    desejada da letra e retorna em que posição da string aquela ocorrência da letra
    está. 
    
        Parameters:
        s: string a ser analisada
        l: letra a ser procurada na string
        num: numero que indica a ocorrência desejada da letra
        
        Returns:
        Retorna a posição da string que aquela letra está, dado que:
        str, str, int -> int
        """
    contador=0
    p=0
    while contador<len(s):
        if num<len(s):
            p=p-1
        elif s in l:
            p=p+s
            str.find(s,l)
        contador=contador+1
    return p