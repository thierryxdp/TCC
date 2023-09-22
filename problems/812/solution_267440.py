def retira_pontuacao(texto):
    test_str = texto
    punc =
    for ele in test_str:  
        if ele in punc:
            test_str = test_str.replace(ele, "")  
return test_str