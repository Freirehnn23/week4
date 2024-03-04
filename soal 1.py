def cek_angka(a, b, c):

    if a != b and a != c and b != c:
        
        if a + b == c or a + c == b or b + c == a:
            return True
        else:
            return False
    else:
        return False

print(cek_angka(4, 2, 3))
print(cek_angka(2, 2, 4))
print(cek_angka(3, 5, 8))
print(cek_angka(2, 6, 8))
