"""1. buat program, deklarasi 5 variabel,
lakukan perhitungan rata-rata 5 nilai tsb tampilkan hasilnya"""

a, b, c, d, e = 3.21, 28, 19, int("13"), 10 # deklarasi 5 variable
print(f"rata-rata : { (a+b+c+d+e)/5 }")

"""2. buat program menghitung luas dan keliling bangun datar 
dengan menerima inputan dari user"""

def luas(a, b): # function menghitung luas
    return a*b

def keliling(a, b): # function menghitung keliling
    return 2*(a+b)

print("menghitung luas dan keliling persegi panjang")
while True: # error handling
    try:
        p = int(input("Panjang = "))
        l = int(input("Lebar = "))
        break
    except ValueError:
        print("input harus berupa integer, coba lagi...")
print(f"Luas = {luas(p,l)} dan keliling = {keliling(p,l)}") #print hasil

"""3. buat program untuk menghitung index 
massa tubuh / BMI (Body mass index) hitung BMI"""
def hitBMI(b, t):
    t = t/100
    hasil = round(b/(t**2), 1)
    if hasil > 0 and hasil < 18.5:
        print(f"BMI anda : {hasil}, masuk dalam kategori Berat Badan Kurang")

    elif hasil >= 18.5 and hasil <= 22.9:
        print(f"BMI anda : {hasil}, masuk dalam kategori Berat Normal")

    elif hasil >= 23 and hasil <= 29.9:
        print(f"BMI anda : {hasil}, masuk dalam kategori Berat Badan Berlebih")

    elif hasil >= 30:
        print(f"BMI anda : {hasil}, masuk dalam kategori Obesitas")

    else:
        print("input anda salah")


print("menghitung BMI")
while True: # error handling
    try:
        b = int(input("Berat Badan (kg) = "))
        t = int(input("Tinggi Badan (cm) = "))
        break
    except ValueError:
        print("input harus berupa integer, coba lagi...")
hitBMI(b,t)
"""4. buat program untuk menentukan nilai maksimal dan minimal 
dari sejumlah nilai masukan N"""

angkaInp = []
while True: # error handling
    try:
        jumInp = int(input("banyak nilai yang akan di Input = ")) #banyak angka yg akan diinput
        break
    except ValueError:
        print("input harus berupa integer, coba lagi...")

for i in range(jumInp): #input semua nilai sesuai jumlah
    while True: #error handling
        try:
            a = int(input(f"Masukkan nilai ke-{i+1} = "))
            break
        except ValueError:
            print("input harus berupa integer, coba lagi...")
    angkaInp.append(a)

nMin = angkaInp[0]
nMax = angkaInp[0]
for j in angkaInp: #mencari nilai min dan max
    if j < nMin:
        nMin = j

    if j > nMax:
        nMax = j

strInp = [str(int) for int in angkaInp]
print(f"angka input : {', '.join(strInp)}") #mencetak hasil
print(f"Nilai Minimal : {nMin}")
print(f"Nilai Maksimal : {nMax}")

"""5. buat program untuk menentukan validasi username dan password, 
dimana akan di ulang maksimal 3 kali, jika benar akan muncul komentar 
” anda berhasil masuk” tapi jika tidak muncul komentar 
” maaf user name dan password anda salah”"""

username0 = 'zulvan'
pass0 = 'fahmi1234'
count = 0

while True:
    un = str(input("Username : ")) #input username dan pass
    pw = str(input("Password : "))

    if un == username0 and pw == pass0: #mencocokan username dan password
        print("anda berhasil masuk")
        break

    else:
        print("Maaf username dan password anda salah") #username / password salah
        count +=1

    if count == 3: #3 kali login gagal program selesai
        print("anda gagal login")
        break


