def concatenacao(a, b):
    """Retorna a concatenação de duas 
strings "a" e "b" no formato abba. 
assinatura: str, str -> str
testes:
concatenacao('a', 'b') == 'abba'
concatenacao('python', 'legal') == 'pythonlegallegalpython'
concatenacao('inicio', 'fim') == 'iniciofimfiminicio'
"""
    return a + b + b + a