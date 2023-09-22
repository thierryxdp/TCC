def hashtag(s):
    palavra = list(s)
    palavra.insert(int(len(palavra)/2),''.join(palavra))
    return ''.join(palavra)