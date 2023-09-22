def conta_frases(frases):
    """Função que recebe um conjunto de frases e retorna quantas frases tem nesse conjunto.
    str -> int
    Explicação: basta analisarmos cada um dos casos, contando a quantidade de frases que terminam em ponto, exclamação e vírgula e corrigindo as reticências para que não sejam entendidas como 3 pontos"""
    reticencias=str.replace(frases,'...','.')
    ponto=str.count(reticencias,'.')
    exclamacao=str.count(frases,'!')
    interrogacao=str.count(frases,'?')
    quantidade=ponto+exclamacao+interrogacao
    return quantidade
# teste 1
# conta_frases('oi, tudo bem?')
# saida esperada: 1
# teste 2
# conta_frases('oi, tudo bem? Faz tempo que não te vejo.')
# saida esperada: 2
# teste 3
# conta_frases('oi, tudo bem? Faz tempo que não te vejo... Vamos sair amanhã! Não ouse faltar.')
# saida esperada: 5