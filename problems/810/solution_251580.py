def invertPalavras(text):
    """Recebe um texto tira qualquer pontuacao e retorna ele invertido com letras minusculas;
    str -->  str"""

    # Torna minuscula e transforma as letras em minusculas
    text = str.lower(text)
    text = substSeparador(text)

    # Separa o texto pelos espacos e inverte e junta
    text = str.split(text)
    list.reverse(text)
    text = str.join(' ', text)

    return text