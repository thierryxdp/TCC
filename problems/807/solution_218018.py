def conta_frases(frase):
    """Retorna a quantidade de frases presentes em uma string, dada na entrada.
    string --> int"""
    conta = int(str.count(frase,('...'))) + int(str.count(frase,'.')) + int(str.count(frase,'?')) + int(str.count(frase,'!'))
    
    return conta