n= int(input('ketik jumlah obyek: '))
r= int(input('ketik jumlah urutan: '))
kombinasi=1
for x in range (kombinasi,n-1):
  kombinasi=kombinasi*x
a=kombinasi
b=n-r
kombinasi=1
for x in range (kombinasi,b-1):
  kombinasi=kombinasi*x
  c=kombinasi
  permutasi=a/c
  print('permutasi dari sejumlah ',n,' obyek dengan urutan sebanyak ',r,' adalah:',permutasi)