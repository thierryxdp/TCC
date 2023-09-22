def posLetra(frase, letra, num):
    '''função que recebe uma string, uma letra e um número que indica
    a ocorrencia da letra na string e retorna em que posicao da string 
    a ocorrencia da letra está; retorna -1 se houver menos ocorrencias
    do que a ocorrencia citada
    str,str,int->int'''
    
    string = str(frase)
    contador = 0
    soma = 0
    while contador<len(string):
        if string[contador]==letra:
                soma = soma+1
                if soma==num:
                    return contador
                else:
                    return -1
        contador = contador+1