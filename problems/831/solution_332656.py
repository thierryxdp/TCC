def lingua_p(palavra):
    """Recebe uma palavra e a transforma para a língua do P (após cada
vogal, um P é inserido e após ele, mais uma vez a vogal que antecede o P.
assinatura: string --> string
testes:
lingua_p('estela') == 'epestepelapa'
lingua_p('avó') == 'apavópó'
"""
    p = p.lower()
    p = str.replace(p, 'a', 'apa')
    p = str.replace(p, 'e', 'epe')
    p = str.replace(p, 'i', 'ipi')
    p = str.replace(p, 'o', 'opo')
    p = str.replace(p, 'u', 'upu')
    p = str.replace(p, 'á', 'ápá')
    p = str.replace(p, 'é', 'épé')
    p = str.replace(p, 'í', 'ípí')
    p = str.replace(p, 'ó', 'ópó')
    p = str.replace(p, 'ú', 'úpú')
    p = str.replace(p, 'ô', 'ôpô')
    return p