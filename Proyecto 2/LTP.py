

def calculate_ltp(m1, m2, w1, w2):
    """
    m1 and m2: mass
    w1 and w2: nonoParameters
    """
    if (m1>0 and m2>0)or (m1<0 and m2<0): #misma carga cada uno
        return 1 + abs(int(m1) - int(m2)) % int(w1)
    else:
        return int(w2) - abs(int(m1) - int(m2)) % int(w2)