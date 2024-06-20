from bentuk.lingkaran import Lingkaran
from bentuk.persegi_panjang import PersegiPanjang

def calculate_properties(bentuk):
    print(f"Luas: {bentuk.luas()}")
    print(f"Keliling: {bentuk.keliling()}")

lingkaran = Lingkaran(5)
persegi_panjang = PersegiPanjang(4, 6)

print("Lingkaran:")
calculate_properties(lingkaran)

print("\nPersegi Panjang:")
calculate_properties(persegi_panjang)
