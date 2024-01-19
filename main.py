import random
import base64

def generowanie_klucz_publicznego(podst_wartosc, klucz_prywatny_osoby, modulo):
    klucz_publiczny_danej_osoby = (podst_wartosc ** klucz_prywatny_osoby) % modulo
    return klucz_publiczny_danej_osoby

def szyfrowanie_wiad(wiadomosc, klucz_szyfr):
    wiad_w_base64 = base64.b64encode(wiadomosc.encode())
    klucz_w_base64 = base64.b64encode(klucz_szyfr.encode())
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
        podstawa , klucz , modulo = dalej.split()
        podstawa = int(podstawa)
        klucz = int(klucz)
        modulo = int(modulo)
        nowy_klucz = generowanie_klucz_publicznego(podstawa,klucz,modulo)
        print(nowy_klucz)
    elif przyklad == "szyfruj":
        pass
    elif przyklad == "odszyfruj":
        pass
    else:
        print("nie znana komenda")
        break
