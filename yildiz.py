def yildiz_olustur(n):
    sonuc = ""
    for i in range(n):
        sonuc += "*" * (i + 1) + "\n"
    return sonuc.strip()
