def conta_frases(texto):
    """Dada um texto, a função conta e retorna a quantidade
    de frases desse texto.
    Parametro de entrada: str
    Retorna: int"""

    tamanhoTexto= len(texto)
  
    listaAuxiliar= texto.split('.')
    tamanho= len(listaAuxiliar)
    if texto[tamanhoTexto-1]!=str('.'):
        tamanho= tamanho-1
        
    listaAuxiliar1= texto.split('?')
    tamanho= tamanho + len(listaAuxiliar1)
    if texto[tamanhoTexto-1]!=str('?'):
        tamanho= tamanho -1

    listaAuxiliar2= texto.split('...')
    tamanho= tamanho + len(listaAuxiliar2)
    if texto[tamanhoTexto-1]!=str('...'):
        tamanho= tamanho -1
        
    listaAuxiliar3= texto.split('!')
    tamanho= tamanho + len(listaAuxiliar3)
    if texto[tamanhoTexto-1]!=str('!'):
        tamanho= tamanho -1
    
    return tamanho-1