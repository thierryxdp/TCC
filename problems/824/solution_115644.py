def uppCons(t):
        return ''.join(c.upper() if c in 'bcdfghjklmnpqrstvxwyz' else c for c in t)