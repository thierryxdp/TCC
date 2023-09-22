def conta_frases(texto):
    frase_nova1=str.replace(texto,'!','.')
    frase_nova2=str.replace(frase_nova1,'?','.')
    frase_nova3=str.replace(frase_nova2,'...','.')
    frase4=str.split(frase_nova3,'.')
    return len(frase4-1)