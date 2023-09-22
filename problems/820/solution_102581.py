#Questao 2
def posLetra(string,l,n):
    '''
    funcao que retorna em que posicao da string esta a ocorrencia da letra.
    str,str,int->int.
    '''
    i = 0
    nr = 0
    
    while i < len(string):
        if string[i] == l:
            nr = nr + 1
            if n == nr:
                return i
        i = i + 1
        
    return -1