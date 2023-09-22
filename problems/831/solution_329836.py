def lingua_p(p):
    """A função traduz a palavra p recebida como parâmetro para a língua do P.
       str -> str
       Explicação: Após cada vogal de p são inseridos as letras p e vogal."""
    l = []
    list.extend(l, p)
    for i in range(len(l)):
        if l[i] in 'AÁEIOÓUaeiouãõôáíéóúê':
           l[i] = l[i] + 'p' + l[i]
    x = 0
    nova_p = ''
    while x < len(l):
        nova_p = nova_p + l[x]
        x = x + 1
    return nova_p
#Testes:
#lingua_p('exemplo')--> 'epexepemplopo'
#lingua_p('caderno')--> 'capadepernopo'
#lingua_p('então')--> 'epentãpãopo'
#lingua_p('corações')--> 'coporapaçõpõepes'
#lingua_p('você')--> 'vopocêpê'
#lingua_p('órgão')--> 'ópórgãpãopo'
#lingua_p('coordenação')--> 'copoopordepenapaçãpãopo'
#lingua_p('saída')--> 'sapaípídapa'
#lingua_p('língua')--> 'lípíngupuapa'