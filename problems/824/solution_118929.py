def uppCons(frase):
    '''funcao que dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas,mantendo todas vogais exatamente como estavam na frase original'''
    lista = list(frase)
    resultado = []
    i = 0
    
    while i < len(lista):
        if lista[i] in 'bcdfghjklmnpqrstvwxyzç':
            resultado.insert(i,lista[i].upper())
            i=i+1
        else:
            resultado.insert(i,lista[i])
            i=i+1
    return ''.join(resultado)