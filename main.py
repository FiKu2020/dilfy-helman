import random

def generowanie_klucz_publicznego(podst_wartosc,klucz_prywatny_osoby,modulo):
    klucz_publiczny_danej_osoby = (podst_wartosc ** klucz_prywatny_osoby) % modulo
    return klucz_publiczny_danej_osoby
def crackowanie_szyfru():
    pass
def szyfrowanie_wiad():
    pass
modulo = 19
podst_wartosc = 6

