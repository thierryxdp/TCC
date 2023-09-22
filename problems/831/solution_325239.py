def lingua_p(s):
    s = [c for c in s]
    return ''.join(s.insert(i+1, 'p'+s[i]) for i in range(len(s)+2) if s[i].lower() in ['a', 'e', 'i', 'o', 'u']