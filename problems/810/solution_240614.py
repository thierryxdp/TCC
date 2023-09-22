def inverte(a):
    """obtemos uma frase, e com ela fazemos operacoes para retornar o inverso
    dela, porem sem alterar as letras contidas nas palavras, tambem retiramos
    qualquer pontuacao contida. Para isso utilizamos o codigo de retirar pontuacao
    retira_pontuacao(a) e aplicamos a funcao str.lower para colocar todas as letras
    em minusculo, separamos as palavras e criamos uma lista, que aplicando a leitura
    inversa dela juntamos a lista de novo para formar uma nova frase.
    string -> string"""
    x=a.replace(".", " ")
    y=x.replace(":", " ")
    z=y.replace(";", " ")
    w=z.replace("-", " ")
    q=w.replace(",", " ")
    e=q.replace("?", " ")
    r=e.replace("!", " ")
    q=r
    q=q.lower()
    q=q.split(" ")
    q=q[::-1]
    q=' '.join(q)
    return q[1:]#a('ab ba. ca') return ca ba ba