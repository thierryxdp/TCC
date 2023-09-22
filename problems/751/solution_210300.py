def quant_palavras(frase):
    """Retorna quantas palavras tem em
uma dada frase, considerando que pode ter
espaços no início e fim, e que as palavras
são separadas por um único espaço.
assinatura: string -> int
casos de testes:
quant_palavras("Python é legal") == 3
quant_palavras("  Python é legal  ") == 3
quant_palavras("Professor Daniel!") == 2
"""
    return len(str.split(frase))