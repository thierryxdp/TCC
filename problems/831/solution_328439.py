def lingua_p(palavra):
    '''Função que recebe uma palavra e traduz para outra língua
    chamada lingua p.
    entrada da função: str
    saída da função: str'''
    
    p = ""
    vog = "aeiouáéíóúãõ"
    for i in palavra:
        if i in vog:
            p = p + (i + "p" + i)
        else:
            p += i
    return str.lower(p)