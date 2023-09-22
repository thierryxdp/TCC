def hashtag(s):
    pre=s[:len(s)//2]
    pos=s[len(s)//2:]
    s = '#'+pre+ '#'+ pos + '#'
    return s