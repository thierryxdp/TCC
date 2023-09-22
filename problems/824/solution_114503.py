def uppCons(frase):
    """funcao que recebe como entrada uma frase e retorna
    essa mesma frase com todas as suas consoantes em 
    maiusculas;
    str -> str"""
    
    nova_frase = ''
    letra = 0
    while letra < len(frase):
        if frase[letra] not in 'AEIOUÁÉÍÓÚÂÊÎÔÛÃÕaeiouáéíóúâêîôûãõü':
            nova_frase = nova_frase + str.upper(frase[letra])
        else:
            nova_frase = nova_frase + frase[letra]
        letra = letra + 1
    return nova_frase