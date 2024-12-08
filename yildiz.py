def yildiz_olustur(n):
    sonuc = ["*" * (i + 1) for i in range(n)]
    return "\n".join(sonuc)
