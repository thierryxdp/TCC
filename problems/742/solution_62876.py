def substitui(s,x,i):
    """
    Funcao que retorna a String(s) com o Caracter(x) no lugar do caracter
    anterior localizado no Indice(i) indicado.
    Parametro de Entrada: string,string,int;
    Valor de Saida: string.
    """
    return str.replace(s,s[i:i+1],x,i)