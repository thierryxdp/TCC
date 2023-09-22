'''Altera uma frase, inserindo uma palavra nova na posição especificada,
ou alterando uma palavra existente para sua versão em maiúsculo.
str, str, int -> str'''
def altera_frase(frase, palavra, pos):
    frase = frase.split()
    if palavra in frase:
        frase[frase.index(palavra)] = palavra.upper()
    else:
        frase.insert(pos,palavra)
    return " ".join(frase)