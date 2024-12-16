import random
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def hasilkan_array(n, seed, nilai_maksimal):
    random.seed(seed)
    return [random.randint(0, nilai_maksimal) for _ in range(n)]

def cek_unik(array):
    return len(array) == len(set(array))

def ukur_waktu_eksekusi(func, *args):
    waktu_mulai = time.perf_counter()  
    hasil = func(*args)
    waktu_selesai = time.perf_counter()  
    return hasil, waktu_selesai - waktu_mulai

# Parameter
nilai_n = [100, 150, 200, 250, 300, 350, 400, 500]  
nilai_maksimal = 250 - 55  # Maksimal nilai elemen array dikurangi dengan NIM saya yaitu F55123055

# Menyimpan hasil
waktu_terburuk = []
waktu_rata_rata = []
semua_waktu_eksekusi = []

# Program utama
for n in nilai_n:
    waktu_eks = []
    print(f"\nMemproses untuk n = {n}...")

    for i in range(5):
        array = hasilkan_array(n, seed=i, nilai_maksimal=nilai_maksimal)
        status_unik = cek_unik(array)
        print(f"Array (n={n}, seed={i}): {array}")
        print(f"Unik: {'Ya' if status_unik else 'Tidak'}")

        _, waktu_eksekusi = ukur_waktu_eksekusi(cek_unik, array)
        waktu_eks.append(waktu_eksekusi)

    semua_waktu_eksekusi.append(waktu_eks)

    waktu_terburuk.append(max(waktu_eks)) 
    waktu_rata_rata.append(sum(waktu_eks) / len(waktu_eks))  

print("\nSemua waktu eksekusi untuk setiap n (dalam detik):")
for n, waktu_eks in zip(nilai_n, semua_waktu_eksekusi):
    print(f"n = {n}: {waktu_eks}")


for n, terburuk, rata_rata in zip(nilai_n, waktu_terburuk, waktu_rata_rata):
    print(f"n = {n} -> Worst Case: {terburuk:.6f} detik, Average Case: {rata_rata:.6f} detik")


plt.figure(figsize=(10, 6))
plt.plot(nilai_n, waktu_terburuk, marker='o', label='Worst Case')
plt.plot(nilai_n, waktu_rata_rata, marker='o', label='Average Case')


plt.title('Worst Case Dan Average Case')
plt.xlabel('Ukuran Array (n)')
plt.ylabel('Waktu Eksekusi (mikrodetik)')


plt.gca().yaxis.set_major_locator(MaxNLocator(integer=False, prune='both'))

plt.grid(True)
plt.legend()

plt.show()
