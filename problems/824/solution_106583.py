def uppCons(frase):
    """Função que recebe uma frase e retorna a frase com todas suas consoantes em maiúsculas e os demais caracteres 
    como estavam
    str -> str"""
    i = 0
    frasenova = ''
    while i < len(frase):
        if str.lower(frase[i]) in 'aeiouáàãâéêíõôó':
            frasenova = frasenova + frase[i]
        else:
            frasenova = frasenova + str.upper(frase[i])
        i = i+1
    return frasenova