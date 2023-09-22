def inverte(frase):
    frase_pontos=retira_pontuaçao(frase)

    frase_dividida=frase_pontos.split()

    list.reverse(frase_dividida)

    frase_final=''.join(frase_dividida).lower()
    return frase_final

print(inverte('um magico nunca revela seus truques!'))