def retira_pontuacao(text):
    """a função retorna uma string com a subistiuição das pontuações por um espaçamento; str->str"""
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace(":", " ")
    text =text.replace(";", " ")
    text = text.replace("-", " ")
    text = text.replace("?", " ")
    text = text.replace("!", " ")
    text = text.replace("...", " ")

    return text