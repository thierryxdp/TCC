def inverte(frase):
    """Recebe uma frase e retorna o contrario da composição das frases.
    str -> str"""

    corrigida = frase.replace('-', ' ').lower
   	corrigida = corrigida.replace(',', ' ')
    corrigida = corrigida.replace(':', ' ')
   	corrigida = corrigida.replace(';', ' ')
   	corrigida = corrigida.replace('.', ' ')
   	corrigida = corrigida.replace('...', ' ')
   	corrigida = corrigida.replace('!', ' ')
    corrigida = corrigida.replace('?', ' ')
        
    txt = corrigida
    separado = txt.split
    return ' '.join(reversed(separado))