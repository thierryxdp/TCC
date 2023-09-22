def inverte(x):
    '''assinatura: str > str
    casos de teste: inverte('oi, bom') ==bom oi
    inverte('muito bem') ==bem muito
    inverte('voce está bem?') ==bem está voce'''
    frase = str.lower(x)
    frase_sempt = retira_pontuacao(frase)
    frase_corta = str.split(frase_sempt,)
    lista_inv = list.reverse(frase_corta)
    frase_inv = str.join(' ', frase_corta)

return frase_inv