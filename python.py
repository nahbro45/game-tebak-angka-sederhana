import random 

print('/////////////////TEBAK ANGKA ////////////////')
print('__________-ANDA PUNYA 5 KESEMPATAN UNTUK MENEBAK______________')

c = random.randint(1,10)
r = 0
max_r = 5   

while(r < max_r):
    b = int(input('pilih angka 1 - 10= '))
    r += 1 

    if ( b < c ):
        print('terlalu kecil ')
    elif( b > c ):
        print ('terlalu besar ')
    elif(b == c ):
        print('//////////kamu benar///////// ')        
if(r == max_r) and ( b != c ):
    print('kesempatanmu habis jawaban yang benar adalah' + str({c}))