def yildiz_olustur(n):
    return "\n".join("*" * i for i in range(1, n + 1))

# def yildiz_olustur(n):
#     if n == 0:
#         return ""
#     return yildiz_olustur(n - 1) + ("\n" if n > 1 else "") + "*" * n
