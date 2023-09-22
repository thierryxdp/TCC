# função consoantes em maiusculo

def uppCons(string):
    '''Dada uma string retorna a mesma com todas as consoantes em maiusculo.
    str -> str'''
    i=0
    nova_string = ''
    while i < len(string):
        if not (string[i] in 'AEIOUaeiouáéíóúãõ'):
            nova_string = nova_string + string[i].upper()
        else:
            nova_string = nova_string + string[i]
        i+=1
    return nova_string