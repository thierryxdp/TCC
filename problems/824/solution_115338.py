def uppCons(frase):
    """Dada uma frase, a função irá transformar todas as consoantes 
    em maiúsculas, e as vogais não sofrerão alteração.
    Tipo da variável frase: string
    Tipo da saída: string"""
    contador = 0
    nova_frase = ''
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZçÇ':
            nova_frase = nova_frase + frase[contador].upper()
		else:
            nova_frase = nova_frase + frase[contador]
        contador = contador + 1
    return nova_frase