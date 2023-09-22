def posLetra(frase,letra,n): 
    '''função chamada (posLetra) que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc). Sua função deve retornar em que posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deveretornar -1.
str,str,int -> int'''
    frase21 = str.replace(frase,letra,'+',n-1) 
    return str.find(frase21,letra)