def retira_pontuacao(potu):
    return str.replace(potu, ',', ' ')
    return str.replace(potu, '.', ' ')
    return str.replace(potu, potu[len(potu) -1], ' ')