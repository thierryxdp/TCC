def hashtag(s):
    def ex6_hashtag(str1):
        s = '#'+ s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return s