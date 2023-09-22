def uppCons(frase):
    """Função que recebe como uma entrada uma frase e retorna a 
    frase com todas as suas consoantes em maiúsculas e as vogais
    minúsculas.
    str -> str"""
    i=0
    lista_str = []
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            list.append(lista_str,frase[i].upper())
        else:
            list.append(lista_str,frase[i])
        i=i+1
    return ''.join(lista_str)