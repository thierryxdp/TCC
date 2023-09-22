def concatenacao(a, b):
    """Retorna a concatenação entre as strings a e b no formato
    abba
    str, str -> str"""
    return a + str(b)*2 + a

# Casos de teste:
# concatenacao(8, 2) == "8228"
# concatenacao("oi", "tudo bem?") == "oitudo bem?tudo bem?oi"
# concatenacao(99, 45) == "99454599"
# concatenacao(-4, 0) == "-400-4"