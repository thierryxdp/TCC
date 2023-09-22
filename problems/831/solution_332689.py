def lingua_p(s):
    """A partir de uma plavra (em português) >s<,
traduz essa palavra para a língua do p, onde as vogais
deverão ser substituídas seguidamente por "p" e a própria
vogal.
assinatura: str --> str
casos de teste:
lingua_p('exemplo') == 'epexepemplopo'
lingua_p('então') == 'epentãopo'
lingua_p('Caderno') == 'capadepernopo'
"""
    s = s.lower()
    s = str.replace(s, 'a', 'apa')
    s = str.replace(s, 'á', 'ápá')
    s = str.replace(s, 'e', 'epe')
    s = str.replace(s, 'é', 'épé')
    s = str.replace(s, 'i', 'ipi')
    s = str.replace(s, 'í', 'ípí')
    s = str.replace(s, 'o', 'opo')
    s = str.replace(s, 'ó', 'ópó')
    s = str.replace(s, 'u', 'upu')
    s = str.replace(s, 'ú', 'úpú')
    return s