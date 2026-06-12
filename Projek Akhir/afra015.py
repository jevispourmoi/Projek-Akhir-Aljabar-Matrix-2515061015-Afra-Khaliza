def transpose_matrix_3x3(matrix):
    hasil = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(3):
        for j in range(3):
            hasil[j][i] = matrix[i][j]

    return hasil


def determinan_3x3(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]

    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]

    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    determinan = (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )

    return determinan


def inverse_matrix_3x3(matrix):

    det = determinan_3x3(matrix)

    if det == 0:
        return None

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]

    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]

    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    kofaktor = [
        [
            (e * i - f * h),
            -(d * i - f * g),
            (d * h - e * g)
        ],
        [
            -(b * i - c * h),
            (a * i - c * g),
            -(a * h - b * g)
        ],
        [
            (b * f - c * e),
            -(a * f - c * d),
            (a * e - b * d)
        ]
    ]

    adjoin = transpose_matrix_3x3(kofaktor)

    inverse = []

    for baris in adjoin:
        baris_baru = []

        for nilai in baris:
            baris_baru.append(nilai / det)

        inverse.append(baris_baru)

    return inverse