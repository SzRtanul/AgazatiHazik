class Auto:
    nev = ""
    gyartasEve = 0

    def __init__(self, nev: str, gyartesEve: int):
        self.nev = nev
        self.gyartasEve = gyartesEve

def flotta(lista: list[Auto]):
    return len(lista)

def legfiatalabb(lista: list[Auto]):
    ind=0
    min= lista[0].gyartasEve
    for i in range(len(lista)):
        if min > lista[i].gyartasEve:
            ind = i
            min = lista[i].gyartasEve
    return lista[ind]

def legoregebb(lista: list[Auto]):
    ind = 0
    max = lista[0].gyartasEve
    for i in range(len(lista)):
        if max < lista[i].gyartasEve:
            ind = i
            max = lista[i].gyartasEve
    return lista[ind]

def main():
    autok = []
    with open("auto.txt", "r") as f:
        for i in f:
            ss = f.readline().split('$')
            autok.append(Auto(ss[0], int(ss[1])))
    print(f"Autók száma: {flotta(autok)}")
    legf = legfiatalabb(autok)
    lego = legoregebb(autok)

    print(f"Legfiatalabb autó:\n"
          f"\tNév: {legf.nev}\n"
          f"\tGyártási év: {legf.gyartasEve}\n")
    print("Legöregebb autó:\n"
          f"\tNév: {lego.nev}\n"
          f"\tGyártási év: {lego.gyartasEve}\n")



if __name__ == '__main__':
    main()