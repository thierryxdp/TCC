def retira_pontuacao(texto):
    test_str = texto
    for ele in test_str:
        test_str = test_str.replace(ele, "")
    return test_str