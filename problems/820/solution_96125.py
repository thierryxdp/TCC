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
    if s.count(l)<num:
        return -1
    else:
        contador=0
        t=[]
        k=list(s)
        while contador<len(k) and len(t)<num:
            if l==k[contador]:
                list.append(t,k[contador])
            contador=contador+1
    return contador-1