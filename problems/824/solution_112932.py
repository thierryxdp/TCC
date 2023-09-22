def uppCons(frase):
    """funcao que, dada uma frase de entrada, retorna a frase com todas as consoates maiúsculas e os demais caractere não sao modificados
    str--->str"""
    i=0
    while i<len(frase):
        if frase[i]!='AEIOUaeiou':
            frase= str.replace(frase,frase[i],str.upper[frase[i]],1)
    i=i+1
    return frase