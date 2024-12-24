import time
import matplotlib.pyplot as plt

# --- Fungsi Bubble Sort ---
def bubble_sort(menu):
    """
    Mengurutkan menu berdasarkan harga menggunakan algoritma bubble sort.
    Menghitung dan menampilkan jumlah perbandingan dan waktu eksekusi.
    """
    n = len(menu)
    perbandingan = 0
    start_time = time.time()
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            perbandingan += 1
            if menu[j][1] > menu[j + 1][1]:
                menu[j], menu[j + 1] = menu[j + 1], menu[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    waktu_eksekusi = end_time - start_time

    # --- Tampilan hasil analisis ---
    print("\n-----------------------------")
    print("Analisis Kompleksitas Bubble Sort")
    print("-----------------------------")
    print(f"Jumlah data (n): {n}")
    print(f"Jumlah perbandingan: {perbandingan}")
    print(f"Waktu eksekusi: {waktu_eksekusi:.6f} detik")
    print("-----------------------------")
    print("Kesimpulan:")
    print("Bubble Sort memiliki kompleksitas O(n^2).")
    print("Semakin banyak data, waktu eksekusi meningkat secara kuadratik.")

    return menu

# --- Fungsi untuk Menampilkan Menu ---
def tampilkan_menu(menu):
    """
    Menampilkan menu ke layar.
    """
    print("\nMenu Point Coffee (Terurut berdasarkan tarif):")
    for i, (item, harga) in enumerate(menu):
        print(f"{i+1}. {item}: Rp {harga:,}")

# --- Fungsi Fibonacci ---
def fibonacci_recursive(n):
    """
    Menghitung bilangan Fibonacci ke-n secara rekursif.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """
    Menghitung bilangan Fibonacci ke-n secara iteratif.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# --- Grafik untuk Menyimpan Data ---
n_values = []
recursive_times = []
iterative_times = []

# --- Fungsi untuk Memperbarui Grafik ---
def update_graph():
    """
    Memperbarui grafik perbandingan waktu eksekusi.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label='Recursive', marker='o', linestyle='-')
    plt.plot(n_values, iterative_times, label='Iterative', marker='o', linestyle='-')
    plt.title('Performance Comparison: Recursive vs Iterative')
    plt.xlabel('Input (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Fungsi untuk Mencetak Tabel Waktu Eksekusi ---
def print_execution_table():
    """
    Mencetak tabel perbandingan waktu eksekusi.
    """
    print("\nTabel Perbandingan Waktu Eksekusi:")
    print(f"{'n':<5} {'Recursive Time (s)':<20} {'Iterative Time (s)':<20}")
    min_len = min(len(n_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        print(f"{n_values[i]:<5} {recursive_times[i]:<20.6f} {iterative_times[i]:<20.6f}")

# --- Program Utama ---
menu_point_coffee = [
    ("Espresso", 35000),
    ("Americano", 40000),
    ("Hot/Iced Chocolate", 40000),
    ("Latte", 45000),
    ("Hot/Iced Matcha Latte", 45000),
    ("Red Velvet", 45000),
    ("Cappuccino", 50000),
    ("Caramel Macchiato", 55000),
    ("Mochaccino", 55000),
    ("Piccolo", 55000),
    ("Affogato", 60000),
    ("Vietnamese Drip", 45000),
    ("Kopi Susu Gula Aren", 50000),
    ("Flat White", 50000),
    ("Lemon Squash", 35000),
    ("Ice Lychee Tea", 35000),
    ("Ice Peach Tea", 35000),
    ("Cookies & Cream Frappe", 55000),
    ("Crunchy Caramel Frappe", 55000),
    ("Avocadofee Frappe", 60000),
    ("Matcha Frappe", 60000),
    ("Chocolate Frappe", 60000),
    ("Mysterious Green Frappe", 60000),
    ("Caramel Java Chip Frappe", 65000),
    ("Mocha Frappe", 65000),
    ("Fresh Milk", 30000),
    ("Chocolate Milk", 40000),
    ("Taro Milk", 40000),
    ("Strawberry Milk", 40000),
    ("Red Velvet Milk", 50000),
    ("Matcha Milk", 50000),
]

# --- Urutkan menu berdasarkan harga ---
sorted_menu = bubble_sort(menu_point_coffee.copy())

# --- Tampilkan menu ---
tampilkan_menu(sorted_menu)

# --- Perhitungan Fibonacci ---
for n in range(1, 21):  # Fibonacci dari n=1 hingga n=20
    n_values.append(n)

    # Ukur waktu eksekusi algoritma rekursif
    start_time = time.time()
    fibonacci_recursive(n)
    recursive_times.append(time.time() - start_time)

    # Ukur waktu eksekusi algoritma iteratif
    start_time = time.time()
    fibonacci_iterative(n)
    iterative_times.append(time.time() - start_time)

# Cetak tabel waktu eksekusi
print_execution_table()

# Tampilkan grafik perbandingan
update_graph()
