# P1 = PROJEK MESIN TURING
# Nama  : Ilham Khefi Ramadhanu
# NPM   : 2213020120
# Kelas : 2A

N = 1000 # panjang pita, inisialisasi untuk nilai besar

class TuringMachine:
    def __init__(self, program, input, state=0):
        self.trf = {}
        self.state = str(state)
        self.tape = ''.join(['_']*N)
        self.head = N // 2   # head terletak pada tengah
        self.tape = self.tape[:self.head] + input + self.tape[self.head:]
        for line in program.splitlines():
            s, a, r, d, s1 = line.split(' ')
            self.trf[s,a] = (r, d, s1)

    def step(self):
        if self.state != 'H':
            a = self.tape[self.head]
            action = self.trf.get((self.state, a))
            if action:
                r, d, s1 = action
                self.tape = self.tape[:self.head] + r + self.tape[self.head+1:]
                if d != '*':
                    self.head = self.head + (1 if d == 'r' else -1)
                self.state = s1
                indicator = self.trf.get((self.state, self.tape[self.head]))
                if indicator != None:
                    print(self.tape.replace('_', ''), '|State :', self.state, '|Direction : ', indicator[1])
                else:
                    print(self.tape.replace('_', ''), '|State :', self.state)  
                
    def run(self, max_iter=9999):
        iter = 0
        while self.state != 'H' and iter < max_iter: # mencegah infinity loop
            self.step()
            iter += 1
        result = self.tape.replace('_', '')
        print(result, '|State :', self.state)
        return result

def mainmenu():
    print(f'\nNama  : Ilham Khefi Ramadhanu')
    print(f'NPM   : 2213020120')
    print(f'Kelas : 2A \n')
    
    print("+===================================+")
    print("|  PROGRAM ARITMATIKA MESIN TURING  |")
    print("+===================================+")
    print("| Pilihan Operasi :                 |")
    print("| 1. Penjumlahan                    |")
    print("| 2. Pengurangan                    |")
    print("| 3. Perkalian                      |")
    print("| 4. Pembagian                      |")
    print("+===================================+")
    print("| Masukkan Pilihan Anda (1/2/3/4) : |")
    print("+===================================+")
    
    pil = int(input("Pilihan : "))
    
    if pil == 1:
        print()
        print("+------------------------------------+")
        print("|  OPERASI PENJUMLAHAN MESIN TURING  |")
        print("+------------------------------------+")
        input1 = int(input("Masukkan Bilangan Pertama : "))
        input2 = int(input("Masukkan Bilangan Kedua   : "))
        arr1 = []
        arr2 = []
        bil1 = ''
        bil2 = ''
        for n in range (input1):
            arr1.append('1')
            bil1 = ''.join(arr1)
        for n in range (input2):
            arr2.append('1')
            bil2 = ''.join(arr2)
        print(f"Bilangan Pertama = {bil1}")
        print(f"Bilangan Kedua   = {bil2} \n")
        print("========== PROSES OPERASI ==========")
        operasi = bil1+'0'+bil2 # format 'bil10bil2'
        print(f"{bil1} + {bil2} => {operasi}")
        print(f"{operasi} |State : 0")
        program = open('operasi/penjumlahan.txt').read()
        tm = TuringMachine(program, operasi)
        tm.run()
        bin = tm.run()
        print(f"Hasil => {bin}")
        hasil = len(bin)
        print("====================================")  
        print("Hasil dari ", input1, ' + ', input2, ' = ', hasil) 
        
    elif pil == 2:
        print()
        print("+------------------------------------+")
        print("|  OPERASI PENGURANGAN MESIN TURING  |")
        print("+------------------------------------+")
        input1 = int(input("Masukkan Bilangan Pertama : "))
        input2 = int(input("Masukkan Bilangan Kedua   : "))
        arr1 = []
        arr2 = []
        bil1 = ''
        bil2 = ''
        for n in range (input1):
            arr1.append('1')
            bil1 = ''.join(arr1)
        for n in range (input2):
            arr2.append('1')
            bil2 = ''.join(arr2)
        print(f"Bilangan Pertama = {bil1}")
        print(f"Bilangan Kedua   = {bil2} \n")
        print("========== PROSES OPERASI ==========")
        operasi = bil1+'0'+bil2 # format 'bil10bil2'
        print(f"{bil1} - {bil2} => {operasi}")
        print(f"{operasi} |State : 0")
        program = open('operasi/pengurangan.txt').read()
        tm = TuringMachine(program, operasi)
        tm.run()
        bin = tm.run()
        print(f"Hasil => {bin}")
        hasil = len(bin)
        print("====================================")  
        print("Hasil dari ", input1, ' - ', input2, ' = ', hasil) 
        
    elif pil == 3:
        print()
        print("+------------------------------------+")
        print("|   OPERASI PERKALIAN MESIN TURING   |")
        print("+------------------------------------+")
        input1 = int(input("Masukkan Bilangan Pertama : "))
        input2 = int(input("Masukkan Bilangan Kedua   : "))
        arr1 = []
        arr2 = []
        bil1 = ''
        bil2 = ''
        for n in range (input1):
            arr1.append('1')
            bil1 = ''.join(arr1)
        for n in range (input2):
            arr2.append('1')
            bil2 = ''.join(arr2)
        print(f"Bilangan Pertama = {bil1}")
        print(f"Bilangan Kedua   = {bil2} \n")
        print("========== PROSES OPERASI ==========")
        operasi = bil1+'0'+bil2+'0' # format 'bil10bil20'
        print(f"{bil1} * {bil2} => {operasi}")
        print(f"{operasi} |State : 0")
        program = open('operasi/perkalian.txt').read()
        tm = TuringMachine(program, operasi)
        tm.run()
        bin = tm.run()
        print(f"Hasil => {bin}")
        hasil = len(bin)
        print("====================================")  
        print("Hasil dari ", input1, ' * ', input2, ' = ', hasil)
        
    elif pil == 4:
        print()
        print("+------------------------------------+")
        print("|   OPERASI PEMBAGIAN MESIN TURING   |")
        print("+------------------------------------+")
        input1 = int(input("Masukkan Bilangan Pertama : "))
        input2 = int(input("Masukkan Bilangan Kedua   : "))
        if (input1 < input2):
            print('Angka tidak valid karena pembagi lebih besar')
        else :
            arr1 = []
            arr2 = []
            bil1 = ''
            bil2 = ''
            for n in range (input1):
                arr1.append('1')
                bil1 = ''.join(arr1)
            for n in range (input2):
                arr2.append('1')
                bil2 = ''.join(arr2)
            print(f"Bilangan Pertama = {bil1}")
            print(f"Bilangan Kedua   = {bil2} \n")
            print("========== PROSES OPERASI ==========")
            operasi = bil2+'0'+bil1+'0' # format 'bil10bil20'
            print(f"{bil1} / {bil2} => {operasi}")
            print(f"{operasi} |State : 0")
            program = open('operasi/pembagian.txt').read()
            tm = TuringMachine(program, operasi)
            tm.run()
            bin = tm.run()
            print(f"Hasil => {bin}")
            hasil = len(bin)
            print("====================================")  
            print("Hasil dari ", input1, ' / ', input2, ' = ', hasil)
    else:
        print("Pilihan Tidak Valid")

pil = 0    
mainmenu()