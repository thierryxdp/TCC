def conta_frases(texto):
    '''Escreva um texto. A funcao calcula o numero de frases terminados com
    as seguintes pontuacoes: "!" (exclamacao); "?" (interrogacao;
    "." (ponto final); "..." (reticencias). Obs: Cada fim de frase deve conter
    SOMENTE UMA dessas pontuacoes; Cada vez que aparecer a pontuacao no texto,
    sera considerada final de frase.
    #parametros | in: str (texto de entrada) -> out: int (núm. de frases)'''
    a=texto.count('...') #conta o numero de reticencias
    b=texto.count('.')-3*a #conta a quantidade de pontos. "-3*a" e necessario para nao se repetir a contagem devido as reticencias
    c=texto.count('!') #conta o numero de exclamacoes
    d=texto.count('?') #conta o numero de interrogacoes
    return a+b+c+d