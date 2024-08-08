import random

def oyun():
    kelimeler = ['python', 'bilgisayar', 'mehmet', 'ahmet', 'dosya']
    seçilen_kelime = random.choice(kelimeler)
    hak = 3
    tahmin = set()

    while hak > 0:
        gizli_kelime = " ".join(x if x in tahmin else '_' for x in seçilen_kelime)
        print(gizli_kelime)

        harf_gir = input('Bir Harf Giriniz:  ').lower()

        if harf_gir in tahmin:
            print('Bu Harfi Daha Önce Denediniz!')
        else:
            tahmin.add(harf_gir)
            if harf_gir in seçilen_kelime:
                print('Doğru Tahmin!')
            else:
                hak -= 1
                
                print(f'Yanlış Tahmin! {hak} Hakkınız Kaldı!')

        if all(harf in tahmin for harf in seçilen_kelime):
            print('Tebrikler, kelimeyi doğru tahmin ettiniz:', seçilen_kelime)
            break

    if hak == 0:
        print('Hakkınız Bitti! Kelime:', seçilen_kelime)

oyun()


