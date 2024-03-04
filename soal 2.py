def cek_digit_belakang(a, b, c):

    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10
    
    if digit_a == digit_b or digit_a == digit_c or digit_b == digit_c:
        return True
    else:
        return False

input_a = int(input("Masukkan angka pertama: "))
input_b = int(input("Masukkan angka kedua: "))
input_c = int(input("Masukkan angka ketiga: "))

print(cek_digit_belakang(input_a, input_b, input_c))
