def uppCons(frase):
    '''funcao que dada uma frase retorna todas consoates 
       em maiusculas:parametro de entrada:str, saida:str'''
    i=0
    while i<len(frase):
        if frase[i]  not in 'AEIOUaeiou':
            return str.upper(frase[i])
    else:
        return str.upper(frase[i+1:])
    i=i+1