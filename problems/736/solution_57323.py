def concatenacao(a, b):
    """Função que retorna a concatenação entre duas strings a e b.
    Assinatura: str, str -> str
    Casos de testes:
    concatenacao("bom", "dia") == 'bomdiadiabom'
    concatenacao("machine", "teaching") == 'machineteachingteachingmachine'
    concatenacao("amo", "você") == 'amovocêvocêamo'
    """
    return a+(2*b)+a