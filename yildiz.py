def yildiz_olustur(n):
    yildizlar = []
    for i in range(1, n + 1):
        yildizlar.append("*" * i)
    return "\n".join(yildizlar)
