def lingua_p(palavra):
    """Recebe uma string (palavra em portugues) e retorna uma string (na lingua
do p).
testes: lingua_p('exemplo') == 'epexepemplopo'
lingua_p('entao') == 'epentapaopo'
assinatura: str --> str
"""
    minusculo = palavra.lower()
    posicao = 0
    ret = []
    while posicao < len(minusculo):
        if minusculo[posicao] in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê','î' 'ô','û' 'ã', 'õ','à']:
            ret += [minusculo[posicao]+ 'p' + minusculo[posicao]]
            posicao = posicao + 1
        else:
            ret.append(minusculo[posicao])
            posicao = posicao + 1
    return str.join('', ret)