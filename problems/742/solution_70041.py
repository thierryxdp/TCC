def substitui(s,x,i):
    ''' funcao que a partir dos dados de entrada retorna a string s com novos elementos
        str,str,int --> str '''
    
    if (0 < i < len(s)):
        return s[0:i] + x + s[i+1:]