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

    separado = reversed(txt.split()
    return ' '.join(reversed(separado))