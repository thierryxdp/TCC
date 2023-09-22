substitui(s,x,i):
    ''' funcao que troca de posição um elemento da string por um outro elemento introduzido 
        str,str,int --> str'''
    
    if (0 < i < len(s)):
        
        s[i] = x
        
        return s[0:i] + x + s[i+1:]