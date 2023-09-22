def conta_frases(comentario):
    
    comentario = "Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder a minha aula..."
    comentario = str.replace(comentario,'!','.')
    comentario = str.replace(comentario,'?','.')
    comentario = str.replace(comentario,'...','.')
    comentario = str.split(comentario,'.')
    comentario = str.split(comentario,'-')
    return len(comentario)-1