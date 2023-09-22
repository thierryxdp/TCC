def conta_frases(comentario):
    
    comentario = str.replace(comentario,'!','.')
    comentario = str.replace(comentario,'?','.')
    comentario = str.replace(comentario,'...','.')
    comentario = str.split(comentario,'.')
    return len(comentario)-1