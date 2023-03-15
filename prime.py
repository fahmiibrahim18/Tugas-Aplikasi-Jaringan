import os
import time as tm

a=tm.time()
tm.sleep(2)
print(tm.time()-a)
while True:
    try:
        # masukan angka
        num = int(input("Enter Number= "))
        if num > 1:
            for i in range(2,num):
                # kalo angka bisa dibagi habis (2 s.d. num)
                if num%i == 0:
                    print(f"{num} bukan bilangan prima.\nKarena habis dibagi {i}\n")
                    break
            else:
                print(f'{num} adalah bilangan prima\n') 
                break   
        else:
            print('Harus lebih dari 1')
        
    except:
        print("Harus Angka!\n")
        os.system('cls')

    

    

