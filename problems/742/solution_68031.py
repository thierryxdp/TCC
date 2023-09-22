def substitui(s:str, x:str, i:int) ->str:
    '''retorna uma string igual a s só que na posição i com o elemento x'''
    n=len(s)
    if i==0 :
        return (x + s[1:])
    elif i==n :
        return (s[0:(i-1)]+x)
    elif 0 < i < n :
        return (s[0:(i)] +x + s[i+1:])