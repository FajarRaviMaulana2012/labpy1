#!/user/bin/python3
print ('menentukan bilangan terbesar')
print ('masukan 3 bilanngan yang diinginkan')
a = int (input ('bilangan pertama = '))
b = int (input ('bilangan kedua = '))
c = int (input ('bilangan ketiga = '))
if a>b and a>c :
    print ('bilangan terbesar =',a)
elif b>a and b>c :
    print ('bilangan terbesar =',b)
else :
    print (c,'bilangan terbesar =',c)