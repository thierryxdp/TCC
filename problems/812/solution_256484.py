def retira_pontuacao(texto):
    'Dada uma frase, retorna a frase com a pontuação substituída por espaço. Entrada: str. Saída: str.'
    if '...' in texto:
        texto=str.replace(texto, '...',' ')
    if '.' in texto:
        texto=str.replace(texto, '.',' ')
    if '?' in texto:
        texto=str.replace(texto, '?',' ')
    if '!' in texto:
        texto=str.replace(texto, '!',' ')
    if ',' in texto:
        texto=str.replace(texto, ',',' ')
    if ';' in texto:
        texto=str.replace(texto, ';',' ')
    if ':' in texto:
        texto=str.replace(texto, ':',' ')
    if '-' in texto:
        texto=str.replace(texto, '-',' ')
    return texto