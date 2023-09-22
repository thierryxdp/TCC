def inverte(frase):
    '''Funcao que calcula e retorna uma nova frase sem pontuacao, somente letra minuscula e em ordem reversa.'''
    a1 = str.replace(frase,"-"," ")
    a2 = str.replace(a1,","," ")
    a3 = str.replace(a2,":"," ")
    a4 = str.replace(a3,";"," ")
    a5 = str.replace(a4,"."," ")
    a6 = str.replace(a5,"!"," ")
    a7 = str.replace(a6,"?"," ")
    
    minuscula=str.lower(a7)
    palavras=str.split(minuscula)
    inversa=palavras[::-1]
    return str.join(" ",inversa)