def retira_pontuacao(pontu):
    return str.replace (pontu, ',', ' ')
    return str.replace (pontu, '.', ' ')
    return str.replace (pontu, '?', ' ')
    return str.replace (pontu, '!', ' ')
    return str.replace (pontu, '-', ' ')
    return str.replace (pontu, ':', ' ')
    return str.replace (pontu, ';', ' ')
    return str.replace (pontu, str(pontu[len(pontu)-1]), ' ')