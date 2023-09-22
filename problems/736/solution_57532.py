def concatenacao(a, b):
    """Essa função utiliza duas strings e concatena ambos no formato
    assinatura: str, str -> str
    testes:
    concatenacao('bom','dia')='bomdiadiabom'
    concatenaco('duda','toledo')='dudatoledotoledoduda'
    concatenaco('10h','estudando')='10hestudandoestudando10h'
    """
    return (a+b)+(b[::1]+a[::1])