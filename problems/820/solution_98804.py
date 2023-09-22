def posLetra(frase,l,n):
    """essa funçao recebe uma string frase, uma letra l um numero n que indica a ocorrencia desejada da letra, retornando em que posiçao da string aquela ocorrencia da letra esta"""
    """entrada:str,str,int"""
    """saida:int"""
    	if n>str.count(frase,l):
            return -1