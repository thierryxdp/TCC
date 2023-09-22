def retira_pontuacao (frase):
    """Função que substitui todos os caracteres de pontuação por espaço, dada uma frase
    entrada: str
    saída: str"""
    
    return str.replace(frase, '-' + ':' + ';' + '?' + '!' + '.' + ',', ' ')