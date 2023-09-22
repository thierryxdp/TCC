def substitui(s,x,i):
    '''Essa funçao pega uma string s e troca o elemento de numero i por x.
    str -> str'''
    x = str'x'
    if i>=0 and i<= len(s):
        nova_s = s[0:i] + 'x' + s[i+1:]
        return nova_s