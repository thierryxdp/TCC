def uppCons(frase):
    """Esta função receba uma frase e retorna esta frase com todas as consoantes em maiúsculo, sem alterar os outros caracteres
    str -> str"""
    nova_frase = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            nova_frase += caractere.upper() 
        else:
            nova_frase += caractere
    return nova_frase