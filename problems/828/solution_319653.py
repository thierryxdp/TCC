def primo(n):
"""Função que, dado um número inteiro positivo,
verifica se este é um número primo ou não.
Assinatura: int -> bool
"""
    if qtd_divisores(n) == 2:
        return "True"
    else:
        return "False"