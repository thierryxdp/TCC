def hashtag(s):
    """Retorna uma string s contendo # em seu início, meio e fim.
    str-> str"""
    i = len(s)//2
    return "#" + s[0:i] + "#" + s[i:] + "#"

# Casos de teste:
# hashtag("carlos") == "#car#los#"
# hashtag("hello") == "#he#llo#"
# hashtag("Comovai?") == "#Como#vai?#"