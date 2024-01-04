
def tryInt(szam: str):
    try:
        return True, int(szam)
    except:
        return False, -1

def kor(kor: int):
    szamok=[2023, 2000]
    ertekek = ["friss gyártás", "átlagos korú", "öreg autó"]
    s = ""
    for i in range(0, len(ertekek)):
        if (i > len(szamok)-1 or kor >= szamok[i]):
            s = ertekek[i]
            break
    return s

def main():
    nemszam=True
    while (nemszam):
        s1 = input("Autó neve: ")
        s2 = input("Gyártási dátum: ")
        eh=tryInt(s2)
        if(eh[0] == True):
            nemszam=False
            print(f"Ez az {s1} igazán {kor(eh[1])}.")


if __name__ == '__main__':
    main()