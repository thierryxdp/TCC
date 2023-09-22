def lingua_p(palavra):
    ''' Função que retorna a palavra de entrada traduzida para lingua p. Liguagem p se
    caractriza pela vogal da palavra mais uma letra p antes da propria vogal
    str -> str  '''
    for letra in palavra:
        if letra in 'AÃEIOUaáãeéiouú':
            palavra = (str.replace(palavra,letra,(letra +'p'+ letra)))
    return palavra