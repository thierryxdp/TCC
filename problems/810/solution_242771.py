def inverte(frase):
    """recebe uma frase e retorna a frase invertida, sem pontuação e com as letras minúsculas.
    str -> str
    Explicação: primeiro deixar tudo em minúsculo pois é a função mais 'simples', depois retirar a pontuação e, por fim, mudar a ordem das palavras. Para mudar a ordem precisamos primeiro  separar a frase em palavrs, inverter a ordem delas e adicionar espaços, transformando-as em palavraas em vez de listas."""
    frase=str.lower(frase)
    pontuacao=['...','.','!','?','-',',',':',';']
    for x in pontuacao:
        frase=frase.replace(x,' ')
    frase=(str.split(frase)[::-1])
    frase=' '.join(frase)
    return frase
# teste 1
# inverte('Oi, tudo bem?')
# saida esperada: 'bem tudo oi'