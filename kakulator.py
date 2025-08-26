print('===============KALKULATOR===============')
print(' ')
print(' + = tambah ')
print(' - = kurang ')
print(' * = kali ')
print(' / = bagi ')
print('')
input_pertama = int(input('masukkan angka pertama : '))
op = str(input('masukkan lambang '))
input_kedua = int(input('masukan angka ke dua : '))

if op is '+':
    print('hasil = ' + str(input_pertama + input_kedua))
elif op is '-':
    print('hasil = '+ str(input_pertama - input_kedua))
elif op is '*':
    print('hasil = ' + str(input_pertama * input_kedua))
elif op is '/':
    print('hasil = ' + str(input_pertama / input_kedua))
