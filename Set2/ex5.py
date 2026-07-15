from itertools import combinations


def combinari(x: list, k: int) -> list:
    rezultat = []

    def genereaza(start, combinare_curenta):
        if len(combinare_curenta) == k:
            rezultat.append(tuple(combinare_curenta))
            return
        for i in range(start, len(x)):
            combinare_curenta.append(x[i])
            genereaza(i + 1, combinare_curenta)
            combinare_curenta.pop()

    genereaza(0, [])
    return rezultat

print(combinari([1,2,3,4],3))