def substitui(s,x,i):
    '''Funcao que retorna a string s com o elemento 
    da posicao i substituido pelo caractere x, no 
    qual i e um numero inteiro entre 0 e o comprimento 
    da string.
    Dados de entrada: str, str, int
    Valor de saida: str
    '''
    str_Alterada1 = s[:i]+str(x)+s[i+1:]
    if i<0 or i>=len(s):
        return 'i invalido' 
    return str_Alterada1