def inverte (frase):
    """Função que, dada uma frase, retorna outra que contenha as mesmas palavras, mas na ordem inversa,
    sem letras maiusculas, e sem pontuacao.
    Entrada: String
    Saída: String"""
    
    return str.lower(str.join(' ',(str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'...',' '), '?',' '), '-',' '), ',',' '), ':',' '), ';',' '), '!', ' '), '.',' '))[::-1])))