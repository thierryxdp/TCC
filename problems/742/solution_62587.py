def substitui(s,x,i):
    """ dado uma string (s), uma caraceter (x) e uma posicao (i)(de zero ate o tamanho de s), retormaremos a mesma string porem com o caracter (x) na posicao (i).
        Parametros:
        Entrada -> str,str,int
        Saida   -> str """
    return s[0:i] + x + s[i+1:]