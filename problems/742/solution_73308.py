def substitui(s,x,i):
    '''Retorna a string s trocando o termo na posição i (entre 0 e
    o comprimento de s) por x; str, int, int -> str'''
    antes=s[:i]
    depois=s[i+1:]
    return antes+x+depois