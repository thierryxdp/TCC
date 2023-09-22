def substitui(s,x,i):
    '''Calcule e retorne uma função que receba uma string s, um caractere X e o número inteiro 1, que vai de 0 ao comprimento da string 
    s = () "string"
    x = i
    i = len (s)
    string, int, int --> string '''
    string0=str(s)
    string1=string0[0:i]
    string2=string0[i+1:]
    return str(string1)+str(x)+str(string2)