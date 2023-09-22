def uppCons(texto):
    """Função que recebe como entrada uma frase e retorna a frase com todas as consoantes em maiúsculas"""
    I=0
    frase=''
    while I<len(texto):
        if texto[I] not in 'abcdefjhijklmnopqrstuvwxyzç':
            frase+= texto[I]
        if f[I] in 'abcdefjhijklmnopqrstuvwxyzç':
            texto+=str.upper(texto[I])
            I+=1
        return frase