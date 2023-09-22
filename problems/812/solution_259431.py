def retira_pontuacao(frase, palavra, pos1, pos2):
    '''função que dada uma frase retorna a mesma com todos os caracteres substituídos por espaço'''
    
    index = str.find(frase, palavra, pos1, pos2)
    size = len(palavra)
    
    if (not index == -1) and (pos1 + index + size < pos2):
        pos2 -= index + size - 1
        return frase[:index] + retirar(frase[index + size:], palavra, 0, pos2)
    else:
        return frase[:index] + frase[index + size:]