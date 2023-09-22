# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(str_a, str_b):
    """Funcao que retorna a concatenacao entre as strings str_a
    e a str_b.
    entrada: str, str
    saida: str
    
    parameters:
    str_a: string a
    str_b: string b
    
    Testes:
    concatenacao('Oi', 'Amigo') == OiAmigoAmigoOi
    concatenacao('Ola', 'Mundo') == OlaMundoMundoOla
    """
    return str_a + str_b + str_b + str_a