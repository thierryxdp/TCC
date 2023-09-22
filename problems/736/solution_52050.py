def concatenacao(a: str, b: str) -> str:
    """Concatena duas strings em um formato específico

       Parameters:
       a: Primeira string entre parênteses
       b: Segunda string entre parênteses

       Return:
       A concatenação de duas string no formato "abba", dados os parâmetros
       "a" e "b"

       Examples:
       concatenacao("a", "b") == 'abba'
       concatenacao("oi", ",") == 'oi,,oi'
       concatenacao("a", "a") == 'aaaa'
    """
    return a + b + b + a