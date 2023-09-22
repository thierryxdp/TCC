def uppCons(texto):
    """Função que recebe uma frase e retorna essa frase com todas as suas consoantes em maiúsculo
    entrada: str
    saída: str"""
    i=0
    frase_final=''
    while i<len(texto):
        if texto[i] not in 'aeiou':
            frase_final= frase_final + str.upper(texto[i])
            i=i+1
        else:
            frase_final= frase_final + texto[i]
            i=i+1
    return frase_final