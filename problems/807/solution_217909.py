def conta_frases(comentario):
    """função que dada uma string retorna a quantidade de frases que há na string.
    string -> int"""
    comentario = "Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder a minha aula..."
    comentario = str.replace(comentario,'!','.')
    comentario = str.replace(comentario,'?','.')
    comentario = str.replace(comentario,'...','.')
    comentario = str.split(comentario)
    return len(comentario)