def substitui(s,x,i):
    '''Retorna as substituições desejadas, onde s é a palavra 
    desejada, x é o novo caracter e i é o lugar onde queira 
    substituir o novo caracter;
    string, int, int -> str'''
    
    palavra=s
    return palavra[:i]+x+palavra[i+1:]