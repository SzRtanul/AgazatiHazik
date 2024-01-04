import random

def egyjegyuek_szama(szamok: list[int]):
    egyjegyu=0
    for i in szamok:
        egyjegyu += 1 if(i >= 0 and i <= 9) else 0
    return egyjegyu

def file_kiir(szamok: list[int]):
    with open("szamok.txt", "w") as f:
        f.writelines(f"A fejek száma: {egyjegyuek_szama(szamok)}.")

def main():
    szamok = []
    s=""
    for i in range(5):
        szamok.append(int(random.random() * 99))
    for i in szamok:
        s += f"{i}-"
    print(s.rstrip("-"))
    s = ""
    for i in szamok:
        s += f"{i}; "
    print(f"{s.rstrip('; ')}")
    print(f"Az egyjegyűek száma: {egyjegyuek_szama(szamok)}.")
    file_kiir(szamok)


if __name__ == '__main__':
    main()