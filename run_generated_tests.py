def freq_palavras(frase):
    with open("holder.txt", "a") as file:
        file.write("enter: freq_palavras(frase)" + "\n")
        file.write("dic = {}" + "\n")
        dic = {}
        file.write("lista = frase.split()" + "\n")
        lista = frase.split()
        file.write("for palavra in lista:" + "\n")
        for palavra in lista:
            file.write("if palavra in dic:" + "\n")
            if palavra in dic:
                file.write("dic[palavra] += 1" + "\n")
                dic[palavra] += 1
            else:
                file.write("else:" + "\n")
                file.write("dic[palavra] = 1" + "\n")
                dic[palavra] = 1
        file.write("return dic" + "\n")
        file.write("exit: freq_palavras(frase)" + "\n")
        return dic

def test_1():
    assert freq_palavras("dinheiro é dinheiro e vice versa") == {"dinheiro": 2, "é": 1, "e": 1, "vice": 1, "versa": 1}

def test_2():
    assert freq_palavras("o rato roeu a roupa do rei de roma") == {"o": 2, "rato": 1, "roeu": 1, "a": 1, "roupa": 1, "do": 1, "rei": 1, "de": 1, "roma": 1}

def test_3():
    assert freq_palavras("a vida é bela") == {"a": 1, "vida": 1, "é": 1, "bela": 1}

def test_4():
    assert freq_palavras("python é uma linguagem de programação") == {"python": 1, "é": 1, "uma": 1, "linguagem": 1, "de": 1, "programação": 1}

def test_5():
    assert freq_palavras("o sol nasce para todos") == {"o": 1, "sol": 1, "nasce": 1, "para": 1, "todos": 1}

