import json
hobiL=[]
with open('mahasiswa.json','r') as file:
    data = json.load(file)
    jumlah_maba = int(input('Masukan jumlah mahasiwa baru :'))
    for i in range(jumlah_maba):
        nama = input('Masukan nama Anda :')
        jumlh_hobi = int(input('Masukan Jumlah hobi :'))
        for j in range(1,jumlh_hobi+1):
            hobi = input('Masukkan Hobi ke-'+str(j+1)+" : ")
            hobiL.append(hobi)
        prestasi = input('Masukan Prestasi Anda :')
        data[nama] = [
        {
            "BioData": {
                "Hobi": hobiL
                ,
                "Prestasi": prestasi
            }
        }]
        hobiL.clear()
with open('mahasiswa.json','w') as file:
    json.dump(data, file)