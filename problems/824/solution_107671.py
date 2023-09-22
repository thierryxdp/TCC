def uppCons(frase):
    """Função que dada uma frase, a retorna com todas as consoantes em maiusculo e as vogais da mesma maneira; str -> str"""
    maiuscula = frase.upper()
    vogais = ['a', 'e', 'i', 'o', 'u']
    return maiuscula.lower() in vogais