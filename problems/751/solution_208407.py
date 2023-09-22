def quant_palavras(frase):
    """Função que recebe uma frase e calcula a quantidade de palavras presente na frase.
    str -> int
    Explicação: basta usarmos o split para termos apenas as palavras sem os espaços entre elas e depois o len para contar a quantidade de palavras."""
    return len(str.split(frase))
# teste 1
# quant_palavras('Oi tudo bem')
# saida esperada: 3
# teste 2
# quant_palavras('o cachorro correu até a esquina')
# saida esperada: 6
# teste 3
# quant_palavras('')
# saida esperada: 0