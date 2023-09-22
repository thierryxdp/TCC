def conta_frases(texto):
    '''Função que retorna o número de frases que 
    aparecem neste texto.
    texto=str->list'''
    tipo1 = str.split(texto)
    tipo2 = str.join('',tipo1)
    tipo2 = list.append(list.rstrip('.',tipo2[0]))
    tipo2 = list.append(list.rstrip('!',tipo2[1]))
    tipo2 = list.append(list.rstrip('?',tipo2[2]))
    tipo2 = list.append(list.rstrip('...',tipo2[3]))
    return len(tipo2)