def uppCons(frase):
    '''funcao que dada uma frase retorna todas consoates 
       em maiusculas:parametro de entrada:str, saida:str'''
    i=0
    while i<len(frase):
        if frase[i] not  in 'aeiou':
            return frase[i]
    else:
        return str.upper(frase[i+1:])
    i=i+1