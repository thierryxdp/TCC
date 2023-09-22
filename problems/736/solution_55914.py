""" Função que retorna uma concatenação de duas strings (a e b). 
Assinatura: str, str -> str
Testes:
concatenacao('0', '1') == '0110'
concatenacao('1', '2') == '1221'
"""
def concatenacao(a, b):
     return a + b + b + a