def hashtag(s):
    return '#' +s[:len(s)//2] +s.replace(s,'#') + s[len(s)//2:] + '#'