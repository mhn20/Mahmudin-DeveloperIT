def terbilang(nilai):
    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    output = " "
    n = int(nilai)
    if n>= 0 and n <= 11:
        output = angka[n]
    elif n <20:
        output = terbilang (n-10) + " Belas "
    elif n <100:
        output = terbilang (n/10) + " Puluh " + terbilang (n%10)
    elif n <200:
        output = " Seratus " + terbilang (n-100)
    elif n <1000:
        output = terbilang (n/100) + " Ratus " + terbilang (n%100)
    elif n <2000:
        output = " Seribu " + terbilang (n-1000)
    elif n <1000000:
        output = terbilang (n/1000) + " Ribu " + terbilang (n%1000)
    elif n <1000000000:
        output = terbilang (n/1000000) + " Juta " + terbilang (n%1000000)
    elif n <1000000000000:
        output = terbilang (n/1000000000) + " Milyar " + terbilang (n%1000000000)
    elif n <1000000000000000:
        output = terbilang (n/1000000000000) + " Triliyun " + terbilang (n%1000000000000)
    elif n == 1000000000000000:
        output = "Satu Kuadriliun"
    else:
        output = "Angka Hanya Sampai Satu Kuadriliun"

    return output

def fungsi_loop(tipe=None,modulus1=None,modulus2=None):
    status = ''
    for data in range(1,21):
        reng = data
        if (type(modulus1) is not int and modulus1) or (type(modulus2) is not int and modulus2):
            status = 'error'
            data =  'format berupa angka'
        else:
            if modulus1 and int(modulus1) <= 1:
                status = 'error'
                data =  'angka tidak boleh dibawah 2'
            elif tipe == 'tidak_bisa_dibagi':
                if modulus1 and int(data)%int(modulus1) == 0:
                    data = ""
                else:
                    if modulus2:
                        if int(modulus2) <= 1:
                            status = 'error'
                            data =  'angka tidak boleh dibawah sama dengan 1'
                        else:
                            if int(data)%int(modulus2) == 0:
                                data = ""
            elif tipe == 'bisa_dibagi':
                if modulus2:
                    if int(modulus2) <= 1:
                        status = 'error'
                        data =  'angka tidak boleh dibawah 2'
                    else:
                        if int(data)%int(modulus1) == 0 or int(data)%int(modulus2) == 0:
                            data = terbilang(int(modulus1))+terbilang(int(modulus2))
                else:
                    if modulus1:
                        if int(data)%int(modulus1) == 0:
                            data = terbilang(int(modulus1))
            else:
                if modulus1 and modulus2:
                    data =  'keyword type tidak valid'
        if data:
            if status == 'error':
                if reng == 1:
                    print(data)
            else:
                print(data)

print('Untuk Angka yang bisa dibagi dengan 3 : ')
fungsi_loop('bisa_dibagi',3)
print(' ')

print('Untuk Angka yang bisa dibagi dengan 5 : ')
fungsi_loop('bisa_dibagi',5)
print(' ')

print('Untuk Angka yang bisa dibagi dengan 3 dan 5 : ')
fungsi_loop('bisa_dibagi',3,5)
print(' ')

print('Untuk Angka yang tidak bisa dibagi dengan 3 dan 5 : ')
fungsi_loop('tidak_bisa_dibagi',3,5)
print(' ')