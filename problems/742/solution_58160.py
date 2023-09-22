def substitui(s,x,i):
    ''' Dando como entradas uma string s (colocada entre aspas simples ou 
    duplas), um caractere x (tambem entre aspas) e um numero inteiro i (que 
    vai de 0 ate o comprimento da string s escolhida), a funcao retorna a 
    string s, mas com o caractere x colocado na posicao i escolhida;
    string, int, int -> string '''
    
    return s[0:i] + x + s[i+1:]