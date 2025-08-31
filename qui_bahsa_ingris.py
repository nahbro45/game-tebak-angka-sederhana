print('=============== quiz bahasa ingris =================')
print(' ')
print('pilih tingkat kesulitan quiz ')
print('1.mudah (sd)')
print('2.normal(smp) ')
print('3,susah (sma/smk)')
#lanjutan 

gabung_n = 0
pilih = int(input('pilih : '))
print(' ')
if pilih == 1:
    print('JAWAB PERTANYAAN DI BAWAH INI!!')
    print('pastikan anda mengetik dengan benar ')
    print('====================================')
    print(' ')
    print('1.(apa) dalam bahsa ingris menjadi ? ')
    jawab5 = str(input('jawab: '))
    print(' ')
    if jawab5 == 'what':
        print('jawaban benar✔️')
        a5 = 20
        if a5 == 20:
            gabung_n+=20
        print(f'nilai soal: {a5}')
    else:
        print('jawaban salah❌ ')
        a5 = 0 
        if a5 == 0:
            gabung_n = 0 
        print(f'nilai soal: {a5}')
    print('2.(kamu) dalam bahsa ingris menjadi?  ')
    jawab4 = str(input('jawab: '))
    print(' ')
    if jawab4 == 'you':
        print('jawaban benar✔️ ')
        a4 = 20
        if a4 == 20:
            gabung_n +=20
        print(f'nilai soal: {a4}')
        print('==================')
    else:
        print('jawaban salah❌ ')
        a4 = 0
        if a4 == 0:
            gabung_n +=0
        print(f'nilai soal: {a4}')
        print('==================')
    print('3.(aku) jika dalam bahasa ingris menjadi? ')
    print(' beri 3 jawaban ')
    jawab3 = str(input('jawaban 1; '))
    jawab3_a = str(input('jawaban 2: '))
    jawab3_b = str(input('jawaban 3: '))
    if jawab3 in  ['me','i','my']:
        print('jawaban benar✔️')
    elif jawab3_a == 'i' or 'me' or 'my':
        print('jawaban benar✔️')
    elif jawab3_b == 'my' or 'me' or 'i':
        print('jawaban benar✔️')
    a3 = 20
    if a3 == 20:
        gabung_n +=20
        print(f'nilai soal: {a3}')
    else:
        print('jawaban salah❌ ')
        a3 = 0
        if a3 == 0:
            gabung_n +=0
        print(f'nilai soal: {a3}')
        print('==================')
    print('2.(kita) dalam bahasa ingris menjadi? ') 
    print('beri 2 jawaban ')
    jawab2 =  str(input('jawaban 1:'))
    jawab2_a = str(input('jawaban 2:'))
    if jawab2 in [ 'we','our']:
        print('jawaban 1 benar✔️')
    elif jawab2_a == 'our' or 'we':
        print('jawaban 2 benar✔️')
    a2 = 20
    if a2 == 20:
        gabung_n +=20
        print(f'nilai soal: {a2}')
        print('==================')
    else:
        print('jawaban salah❌')
        a2 = 0
        if a2 == 0:
            gabung_n += 0 
        print(f'nilai soal: {a2}')
        print('==================')
    print('1.(laki laki) dalam bahsa ingris menjadi?  ')   
    jawab1 = str(input('jawaban: '))
    if jawab1 == 'man':
        print('jawaban benar✔️')
        a1 = 20
        if a1 ==  20:
            gabung_n+= 20
        print(f'nilai soal: {a1}')
    else:
        print('jawaban salah❌ ')
        a1 = 0
        if a1 == 0:
            gabung_n+= 0
        print(f'nilai soal: {a1}')
    print(' ')
    print('==========================================')
    print(f'total nilai keseluruhan soal: {gabung_n}')
    if gabung_n == 100:
        print('bagus⭐⭐⭐')
    elif gabung_n == 80:
        print('not bad')
    elif gabung_n == 60:
        print('perlu belajar lagi')
    elif gabung_n == 40:
        print('benar benar perlu belajar lagi ')
    else:
        print('sungguh anda perlu belajar lagi belajar lagi👌👌')
    print('==========================================')

if pilih == 2:
    print('JAWAB PERTANYAAN DI BAWAH INI!!')
    print('pastikan anda mengetik dengan benar ')
    print('====================================')
    print(' ') 
    print('1. Which of the following phrases can be used to express sadness when saying goodbye to someone?')
    print('A. It was nice to see you.')
    print('B. Have a safe trip!') 
    print('C. See you soon!') 
    print('D. I will miss you.' ) 
    jawab5 = str(input('jawab: '))
    if jawab5 == 'd' or 'D':
        print('jawaban benar✔️')
        a5 = 20 
        if a5 == 20:
            gabung_n +=20
        print(f'nilai soal: {a5}')
        print('===================')
    else:
        print('jawaban salah❌')
        a5 = 0 
        if a5 == 0:
            gabung_n +=0
        print(f'nilai soal: {a5}')
        print('=====================')
    print('2. ... you have a science class on Wednesday?')
    print('A. Is')
    print('B. Are')
    print('C. Do')
    print('D. Does')
    jawab4 = str(input('jawaban: '))
    if jawab4 == 'c' or 'C':
        print('jawaban benar✔️')
        a4 = 20
        if a4 == 20:
            gabung_n +=20
        print(f'nilai soal: {a4}')
        print('======================')
    else:
        print('jawaban salah❌')
        a4 = 0 
        if a4 == 0:
            gabung_n +=0
        print(f"nilai soal: {a4}")
        print('======================')
    print('3.What would you say if you want to ask about someone"s condition?')
    print('A. Good afternoon')
    print('B. Hi, how are you?')
    print('C. Good night')
    print('D. Glad to see you')
    jawab3 = str(input('jawaban: '))
    if jawab3 == 'b' or 'B':
        print('jawaban benar✔️')
        a3 = 20 
        if a3 ==20:
            gabung_n +=20
        print(f'nilai soal: {a3}')
        print('=======================')
    else:
        print('jawaban salah❌')
        a3 = 0 
        if a3 == 0:
            gabung_n+=0
        print(f'nilai soal: {a3}')
        print('========================')
    print('4.Read the conversation carefully!')
    print(' ')
    print('John: Hi, my name is John. Nice to meet you.')
    print('Sarah: Hi, John. Nice to meet you too. My name is Sarah. ____________')
    print('Which one is the best answer to complete the blank space to express greetings?')
    print('A. Where are you from?')
    print('B. How old are you?')
    print('C. How do you do?')
    print('D. I hate you.')
    jawab2 = str(input('jawaban: '))
    if jawab2 == 'c' or 'C':
        print('jawaban benar✔️')
        a2 = 20
        if a2 == 20 :
            gabung_n+=20
        print(f'nilai soal: {a2}')
        print('===================')
    else:
        print('jawaban salah❌')
        a2 = 0 
        if a2 == 0:
            gabung_n +=0
        print(f'nilai soal; {a2}')
        print('=====================')
    print('5.read th converaati0n carefully!!')
    print(' ')
    print('Vina: Can you water the plant soon?')
    print('Nina: ..... I have to wash dishes before I water it?')
    print('Which one is the best answer to complete the blank space?')
    print("A. No, I'm not")
    print("B. No, I can't")
    print("C. No. I don't")
    print("D. No, I won't")
    jawab1 = str(input('jawaban: '))
    if jawab1 == 'b' or 'B':
        print('jawaban benar✔️')
        a1 = 20
        if a1 == 20:
            gabung_n +=20
        print(f'nilai soal: {a1}')
        print('=======================')
    else:
        print('jaaban salah❌')
        a1 = 0 
        if a1 == 0:
            gabung_n +=0
    print(f'nilai soal: {a1}')
    print('=======================================')
    print(f'nilai keseluruhan: {gabung_n}') 
    if gabung_n == 100:
        print('bagus⭐⭐⭐')
    elif gabung_n == 80:
        print('not bad ')
    elif gabung_n == 60:
        print('perlu belajar lagi')
    elif gabung_n == 40:
        print('anda perlu belajar lagi ')
    else:  
        print('ana benar benar perlu belajar lagi👌👌')
    print('========================================')

if pilih == 3:
    print('JAWAB PERTANYAAN DI BAWAH INI!!')
    print('pastikan anda mengetik dengan benar ')
    print('====================================')
    print(' ')
    print('1. Indy: The box you brought looks very heavy. ......................................')
    print("   Putri: Sure, it's very kind of you. Thanks.")
    print('   The suitable expression to complete the dialogue is...')
    print('   A. Would you like to help me?')
    print('   B. Would you love to help us?')
    print('   C. Could you bring it for me?')
    print('   D. Would you like me to help you?')
    print('   E. Would you like me to bring it for myself?')
    jawab5 = str(input('jawaban: '))
    if jawab5 == 'd' or 'D':
        print('jawaban benar✔️')
        a5 = 20 
        if a5 == 20:
            gabung_n +=20
        print(f'nilai soal: {a5}')
        print('==============================')
    else:
        print('jawaban salah❌')
        a5 = 0 
        if a5 == 0:
            gabung_n +=0
        print(f'nilai soal: {a5}')
        print('=============================')
    print('2.Do you bring the book ... I gave it to you yesterday?')
    print('  A. When') 
    print('  B. That')
    print('  C. Where')
    print('  D. How ')
    print('  E. Which') 
    jawab4 = str(input('  jawaban: '))
    if jawab4 == 'e' or 'E':
        print('jawaban benar✔️')
        a4 = 20
        if a4 == 20:
            gabung_n +=20
        print(f'nilai soal: {a4}')
        print('============================')
    print('3.Every night the watchman turns on all the lights and ... around the building every half an hour.')
    print('  A. Walk')
    print('  B. Is walking')
    print('  C. To be walking')
    print('  D. Walking') 
    print('  E. To walk')
    jawab3 = str(input('jawaban: '))
    if jawab3 == 'a' or 'A':
        print('jawaban benar✔️')
        a3 = 20
        if a3 == 20:
            gabung_n +=20
        print(f'nilai soal: {a3}')
        print('===========================')
    else:
        print('jawaban salah❌')
        a3 = 0 
        if a3 == 0.:
            gabung_n +=0 
        print(f'nilai soal: {a3}')
        print('==========================')
    print(". X: I think we're going to be here for a while")
    print('  Y: But we ... in line for almost an hour')
    print('  A. Are standing')
    print('  B. Have stood')
    print('  C. Stand')
    print('  D. Were standing')
    print('  E. Have been standing')
    jawab2 = str(input('jawaban: '))
    if jawab2 == 'e' or 'E':
        print('jawaban benar✔️')
        a2 = 20 
        if a2 == 20:
            gabung_n +=20 
        print(f'milai keseluruhan: {a2}')
        print('==============================')
    else:
        print('jawaban salah❌')
        a2 = 0 
        if a2 == 0:
            gabung_n +=0
        print(f'nilai soal: {a2}')
        print('===========================----')
    print('1.Can we postpone the class meeting until Friday?')
    print("  I'm afraid not. I ... basketball on Friday.")
    print('  A. Would play')
    print('  B. Will have been playing')
    print('  C. Have been playing')
    print('  D. Always play')
    print('  E. Played')
    jawab1 = str(input('jawaban: '))
    if jawab1 == 'd' or 'D':
        print('jawaban benar✔️')
        a1 = 20 
        if a1 == 20:
            gabung_n +=20
        print(f'nilai soal: {a1}')
        print('=============================')
    else:
        print('jawaban salah')
        a1 = 0 
        if a1 == 0:
            gabung_n += 0 
        print(f'nilai soal; {a1}')
        print('================================')
        print(' ')
    print('======================================================')
    print(f'nilai keseluruhan: {gabung_n}')
    if gabung_n == 100:
        print('nice ⭐⭐⭐')
    elif gabung_n == 80:
        print('not bad!!')
    elif gabung_n == 60:
        print('belajar lagi!!')
    elif gabung_n == 40:
        print('you need more study')
    else:
        print('fix you need more study')
print(' ')
print('========================================')
     