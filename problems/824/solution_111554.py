def uppCons(frase):
    """Função que dada uma frase, retorna esta com todas suas consoantes maiúsculas
str -> str"""

    nova_frase = ''
    caractere = 0

    while caractere <len(frase):
        if (frase[caractere]) in 'bcçdfghjklmnpqrstvwxyz':
            nova_frase = nova_frase + frase[caractere].upper()
            caractere = caractere + 1
        else:
            nova_frase = nova_frase + frase[caractere]
            caractere = caractere + 1
    return nova_frase