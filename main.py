import random
import base64
import hashlib
def generowanie_klucz_publicznego(podst_wartosc, klucz_prywatny_osoby, modulo):
    klucz_publiczny_danej_osoby = (podst_wartosc ** klucz_prywatny_osoby) % modulo
    return klucz_publiczny_danej_osoby
def crackowanie_szyfru():
    pass
def szyfrowanie_wiad(wiadomosc, klucz_szyfr):
    zaszyfr_wiad = ""
    wiad_w_base64 = base64.b64encode(wiadomosc.encode())
    print(wiad_w_base64)
def odzszyfr_wiad(wiadomosc,klucz_szyfr):
    pass
modulo = 19
podst_wartosc = 6
przyklad = str(input(">"))
print(szyfrowanie_wiad(przyklad, 10))