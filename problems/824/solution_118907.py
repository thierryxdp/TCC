def uppCons(frase):
    '''Funcao que dada uma frase retorna a mesma com todas
    as suas consoantes em maiusculas
    Parametro:
    Str
    Saida:Str'''
    l=frase
    p=0
    while p< len(frase):
        if frase[p] != "a" and != "e" and != "i" and != "o" and != "u":
            l= l+ str.upper(frase[p])
        p= p +1
        
    return l