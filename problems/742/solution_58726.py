def substitui(s,x,i):
    ''' função que retorna a string 's' com a alteração do elemento na
        posição 'i' pelo caractere 'x'
        [str,str,int--> str]'''
    return s[:i] + x + s[(i+1):]