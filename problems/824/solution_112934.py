def uppCons(frase):
    """funcao que, dada uma frase de entrada, retorna a frase com todas as consoates maiúsculas e os demais caractere não sao modificados
    str--->str"""
    i=0
    frase_nova=''
    while i<len(frase):
        if frase[i]!='AEIOUaeiou':
            str.upper(frase)
            frase_nova=frase_nova+frase[i]
        else:
            frase_nova=frase_nova+frase[i]
        i=i+1
    return frase_nova