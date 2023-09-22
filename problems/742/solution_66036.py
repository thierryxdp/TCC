def substitui(s,x,i):
    '''Essa funçao pega uma string s e troca o elemento de numero i por uma outra letra a escolha do usuario.
    str -> str'''
    
        if i>=0 and i<= len(s):
        nova_s = s[0:i] + str x + s[i+1:]
        return nova_s