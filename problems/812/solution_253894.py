def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase só que sem pontuação; string->string"""
    if '-' in frase:
        s = str.replace(frase, '-', ' ')
        elif ',' in frase:
            p = str.replace(s, ',', ' ')
            elif  '.' in frase:
                return str.replace(p, '.', ' ')