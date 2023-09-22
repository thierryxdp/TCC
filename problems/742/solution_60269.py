def substitui(s,x,i):
    '''substitui o caractere x na posição i da string s
    	str, int, str -> str'''
    
    if i<= len(s):
        return str.replace(s,len(s)==i,"x",1)
    
    else:
        return False