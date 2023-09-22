def lingua_p(palavra):
    '''Funcao que recebe uma palavra em portugues e retorna 
    a sua traducao na ligua do P, em letras minusculas.
    str -> str'''
    palavraL = str.lower(palavra)
    traducao = ''
    for letra in palavraL:
        traducao = traducao + letra #aqui eu add a letra na traducao para dps add a 'fatia' com o p
        if letra in 'AEIOUaeiouÁÉÍÓÚáéíóúÂÊÔâêôãõ':
            traducao = traducao + 'p' + letra
    return traducao

#TESTES
# lingua_p('oftamologista') == 'opoftapamopolopogipistapa'
# lingua_p('Ipanema') == 'ipipapanepemapa'
# lingua_p('mamão') == 'mapamãpãopo'