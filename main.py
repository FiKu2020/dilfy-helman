import random
import base64
import hashlib

def generowanie_klucz_publicznego(podst_wartosc, klucz_prywatny_osoby, modulo):
    klucz_publiczny_danej_osoby = (podst_wartosc ** klucz_prywatny_osoby) % modulo
    return klucz_publiczny_danej_osoby

def szyfrowanie_wiad(wiadomosc, klucz_szyfr):
    wiad_w_base64 = base64.b64encode(wiadomosc.encode())
    klucz_w_base64 = base64.b64encode(klucz_szyfr)
    zaszyfr_wiad = wiad_w_base64.encode(klucz_szyfr).decode()
    return zaszyfr_wiad
def odzszyfrowanie_wiad(wiadomosc,klucz_szyfr):
    czytelna_wiad = base64.b64decode(wiadomosc.decode)
    czytelny_klucz = base64.b64decode(klucz_szyfr.decode)

while True:
    przyklad = str(input(">"))
    if przyklad == "stop":
        break
    elif przyklad == "klucz":
        print("podaj: podstawowa wartosc , klucz prywatny oraz wartosc modulo")
        dalej = input(">")
        podstawa , klucz , modulo = int(dalej.split())
        podstawa = int(podstawa),
        klucz = int(klucz)
        modulo = int(modulo)
        nowy_klucz = generowanie_klucz_publicznego(podstawa,klucz,modulo)
        print(nowy_klucz)
    elif przyklad == "szyfruj":
        dalej = input(">")
        wiad , klucz = dalej.split()
        wiad = str(wiad)
        klucz = int(klucz)
        print(szyfrowanie_wiad(klucz,wiad))
    elif przyklad == "odszyfruj":
        dalej = input(">")
        zaszyfr_wiad , klucz_odszyfr = dalej.split()
        print(odzszyfrowanie_wiad(zaszyfr_wiad,klucz_odszyfr))
    else:
        print("nie znana komenda")
        break
