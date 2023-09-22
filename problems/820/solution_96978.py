def posLetra (frase1, l, n):
    """função que recebe uma frase (frase1), uma letra (l) e um número
    (n) e que deve analisar a frase e encontrar a posição da letra de
    entrada, tal que seja procurada a ocorrência referente ao número 
    (n) de entrada. E que deve retornar a posição <p> que se encontra 
    a letra;
    str,str,int->int"""
    p = 0
    qtd_letra = str.count(frase1,l)
    n_letra = []
    p_letra = 0
    if qtd_letra<n:
        return -1
    while len(frase1)>p:
        if frase1[p]==l:
            p_letra = [str.index(frase1,l)]
            frase1 = str.replace(frase1,frase1[p],' ',1)
            n_letra = n_letra + [p_letra]
        p = p+1
    return n_letra[n-1]