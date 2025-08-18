import random 

print('/////////////////TEBAK ANGKA ////////////////')
print('|___________________________________________|')
print('                                             ')
print('^> cara bermain')
print('-------------------------------------------------------')
print('^> kalinn akan bermain dengan komputer ')
print('-------------------------------------------------------')
print('^> ANDA PUNYA 5 KESEMPATAN UNTUK MENEBAK')
print('-------------------------------------------------------')
print("^> komputer akan menjawab dengan input (komputer: )")
print('--------------------------------------------------------')
print(' ')
print('===== selamat bermain dan semoga beruntung =========')
print('----------------------------------------------------')

c = random.randint(1,10)
r = 0
max_r = 5   

while(r < max_r):
    b = int(input('komputer: pilih angka 1 - 10= '))
    r += 1 

    if ( b < c ):
        print('komputer: terlalu kecil ')
        print('                           ')
    elif( b > c ):
        print ('komputer: terlalu besar ')
        print('                               ')
    else:
        print('komputer:  selamat kamu benar ')
        print('KAMU MANDAPAT 3 BINTANG')
        exit(0)
    print('kesempatan anda tinggal: ' + str(max_r - r))
    print('-------------------------------------------------')
    print('     ')
print('anda gagal ')
print('mision filed')
