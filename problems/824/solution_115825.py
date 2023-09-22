def uppCons(t):
        return ''.join(c.upper() if c in 'bcdfghjklmnpqrstvxwyzç' else c for c in t)