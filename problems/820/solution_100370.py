def posLetra(string, letra, num):
    '''sao dados uma frase, uma letra e um numero, e retorna a posicao
       da num dela na frase, e caso nao tenha, retorna -1
       str, str, int -> int'''
    
    a=1
    b=-1
    
    while a<=num:
        if a!=num:
            string=str.replace(string, letra, '#', 1)
        else:    
            b=str.find(string, letra)
        a=a+1    
    return b