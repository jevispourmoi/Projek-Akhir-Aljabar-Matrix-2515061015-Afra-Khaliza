def transpose(m):
    return [[m[j][i] for j in range(3)] for i in range(3)]


def determinan(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)


def inverse(m):
    det = determinan(m)
    if det == 0:
        return None

    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]

    kofaktor = [
        [ (e*i - f*h), -(d*i - f*g),  (d*h - e*g)],
        [-(b*i - c*h),  (a*i - c*g), -(a*h - b*g)],
        [ (b*f - c*e), -(a*f - c*d),  (a*e - b*d)]
    ]

    return [[x / det for x in baris] for baris in transpose(kofaktor)]