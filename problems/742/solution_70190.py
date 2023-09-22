def substitui(s,x,i=0):
    '''retorna a string s porém com seu elemento de posição i substituido por x'''
    '''str,str,int->str'''
    comprimento = len(s)
    if 0<=i<comprimento:
        return (s[:i])+str(x)+(s[(i+1):])
    else:
        return 'i inválido'