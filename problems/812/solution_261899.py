def retira_pontuacao (frase):
    """Função que, dada uma frase, retorna com todos os caracteres de pontuação substituídos por espaço
    entrada:string
    saída:string"""
    if '-' in frase:
        frase=str.replace(frase,'-',' ')
    if ',' in frase:
        frase=str.replace(frase,',',' ')
    if ':' in frase:
        frase=str.replace(frase,':',' ')
    if ';' in frase:
        frase=str.replace(frase,';,' ')
    if '!' in frase:
        frase=str.replace(frase,'!',' ')
    if '?' in frase:
        frase=str.replace(frase,'?',' ')
    if '...' in frase:
        frase=str.replace(frase,'...',' ')
    if '.' in frase:
        frase=str.replace(frase,'.',' ')
    return frase