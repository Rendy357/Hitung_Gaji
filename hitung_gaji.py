def hitung_gaji(jam_kerja, tarif_per_jam):
    # Jika jam kerja lebih dari 40, hitung gaji lembur
    if jam_kerja > 40:
        jam_lembur = jam_kerja - 40
        gaji_biasa = 40 * tarif_per_jam
        gaji_lembur = jam_lembur * (tarif_per_jam * 1.5)
        total_gaji = gaji_biasa + gaji_lembur
    else:
        total_gaji = jam_kerja * tarif_per_jam
    
    return total_gaji

def main():
    # Meminta input dari pengguna
    jam_kerja = float(input("Masukkan jumlah jam kerja: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))
    
    # Menghitung gaji
    total_gaji = hitung_gaji(jam_kerja, tarif_per_jam)
    
    # Menampilkan hasil
    print(f"Gaji karyawan adalah: Rp {total_gaji:.2f}")

if __name__ == "__main__":
    main()