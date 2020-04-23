#syntak pertama
print('hello word')
message = 'hello world'
nama = 'Anda KauDia'
lingkar_perut = 30.5
usia = 16  #usia adalah angka dan string
print(message)
print(nama)
print(usia)
print (lingkar_perut)

if usia < 17 :
    print ('Belum boleh nonton film 18 tahun ke atas yaks!')
    print ('Muda cuy')
else:
    print ('Mayan tua..')

if usia < 30 :
    print ('Sudah bangun!')
elif lingkar_perut < 40:
    print ('susah pakai seat belt ya')
else:
    print ('bahaya')

for i in range(2, 3):
    print(message)

while usia > 0:
    print('usia saat ini %s' % usia)
    print('masih hidup')
    usia = usia-1
#yang komplek di python adalah list atau array
#pemogram python itu array dan dikseneri

daftar_nama=['saya', 'aku','I','myself']
print (daftar_nama)
daftar_nama.append('abdi')
daftar_nama.append('kulo')
print (daftar_nama)

for dn in daftar_nama:
    print('nama lain anda adalah %s, padahal nama aslimu itu %s lho!' % (dn, nama))
#using dictonary
#dictonary adalah tipe adalah aspek modern oop
#memiliki tipe data dictonaru di python
#dictonary bisa di extrax file json
#json adalah tipe data komuninkasi antar web function dari yang berbeda-beda
#dictonaru pikirkan manusia dan attributnya

manusia = {}
manusia['nama'] ='prabowo'
manusia['sex'] ='laki-laki'
manusia['status'] = 'menikah'
print (manusia)
manusia['nama'] = 'Prabowo widokdo'
print (manusia)
manusia['alamat']='jakarta'
print (manusia)

#import json
import json
print(json.dumps(manusia))

