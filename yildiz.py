def yildiz_olustur(n):
    if n == 0:
        return ""
    return yildiz_olustur(n - 1) + ("\n" if n > 1 else "") + "*" * n
