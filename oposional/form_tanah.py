import tkinter as tk
from tkinter import ttk, messagebox
from koneksi import create_connection

def form_tanah():
    db = create_connection()
    cursor = db.cursor()
    cursor.execute('use dataset_lahan')

    # Fungsi untuk menambahkan data dari form input ke database
    def add_reading():
        try:
            nama = nama_entry.get()
            min_C1 = float(min_C1_entry.get())
            max_C1 = float(max_C1_entry.get())
            min_C2 = float(min_C2_entry.get())
            max_C2 = float(max_C2_entry.get())
            min_C3 = float(min_C3_entry.get())
            max_C3 = float(max_C3_entry.get())
            min_C4 = float(min_C4_entry.get())
            max_C4 = float(max_C4_entry.get())
            min_C5 = float(min_C5_entry.get())
            max_C5 = float(max_C5_entry.get())

            sql = """
            INSERT INTO tanah (nama, min_C1, max_C1, min_C2, max_C2, min_C3, max_C3, min_C4, max_C4, min_C5, max_C5)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            val = (nama, min_C1, max_C1, min_C2, max_C2, min_C3, max_C3, min_C4, max_C4, min_C5, max_C5)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Success", "Record inserted successfully!")
            get_readings()  # Refresh tabel setelah insert
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

    # Fungsi untuk membaca data dari database dan menampilkan dalam tabel
    def get_readings():
        cursor.execute("SELECT * FROM tanah")
        rows = cursor.fetchall()

        # Hapus data yang sudah ada di Treeview
        for i in tree.get_children():
            tree.delete(i)

        # Masukkan data yang baru
        for row in rows:
            tree.insert("", "end", values=row)

    # Fungsi untuk memperbarui data di database
    def update_reading():
        try:
            record_id = int(id_entry.get())
            nama = nama_entry.get()
            min_C1 = float(min_C1_entry.get())
            max_C1 = float(max_C1_entry.get())
            min_C2 = float(min_C2_entry.get())
            max_C2 = float(max_C2_entry.get())
            min_C3 = float(min_C3_entry.get())
            max_C3 = float(max_C3_entry.get())
            min_C4 = float(min_C4_entry.get())
            max_C4 = float(max_C4_entry.get())
            min_C5 = float(min_C5_entry.get())
            max_C5 = float(max_C5_entry.get())

            sql = """
            UPDATE tanah SET nama = %s, min_C1 = %s, max_C1 = %s, 
            min_C2 = %s, max_C2 = %s, min_C3 = %s, max_C3 = %s, 
            min_C4 = %s, max_C4 = %s, min_C5 = %s, max_C5 = %s 
            WHERE id = %s
            """
            val = (nama, min_C1, max_C1, min_C2, max_C2, min_C3, max_C3, min_C4, max_C4, min_C5, max_C5, record_id)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Success", "Record updated successfully!")
            get_readings()  # Refresh tabel setelah update
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

    # Fungsi untuk menghapus data dari database
    def delete_reading():
        try:
            record_id = int(id_entry.get())
            sql = "DELETE FROM tanah WHERE id = %s"
            val = (record_id,)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Success", "Record deleted successfully!")
            get_readings()  # Refresh tabel setelah delete
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid ID.")

    # Membuat GUI menggunakan Tkinter
    root = tk.Tk()
    root.title("Tanah Data Input")

    # Mengatur posisi window di tengah layar
    window_width = 400
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height/2 - window_height/2)
    position_right = int(screen_width/2 - window_width/2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Frame untuk form input di tengah
    form_frame = tk.Frame(root)
    form_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor='w')

    # Label dan Entry untuk input ID (untuk update dan delete)
    tk.Label(form_frame, text="ID (for update/delete):").grid(row=0, column=0)
    id_entry = tk.Entry(form_frame)
    id_entry.grid(row=0, column=1)

    # Label dan Entry untuk input Nama
    tk.Label(form_frame, text="Nama:").grid(row=1, column=0)
    nama_entry = tk.Entry(form_frame)
    nama_entry.grid(row=1, column=1)

    # Label dan Entry untuk input rentang C1
    tk.Label(form_frame, text="Min C1:").grid(row=2, column=0)
    min_C1_entry = tk.Entry(form_frame)
    min_C1_entry.grid(row=2, column=1)

    tk.Label(form_frame, text="Max C1:").grid(row=3, column=0)
    max_C1_entry = tk.Entry(form_frame)
    max_C1_entry.grid(row=3, column=1)

    # Label dan Entry untuk input rentang C2
    tk.Label(form_frame, text="Min C2:").grid(row=4, column=0)
    min_C2_entry = tk.Entry(form_frame)
    min_C2_entry.grid(row=4, column=1)

    tk.Label(form_frame, text="Max C2:").grid(row=5, column=0)
    max_C2_entry = tk.Entry(form_frame)
    max_C2_entry.grid(row=5, column=1)

    # Label dan Entry untuk input rentang C3
    tk.Label(form_frame, text="Min C3:").grid(row=6, column=0)
    min_C3_entry = tk.Entry(form_frame)
    min_C3_entry.grid(row=6, column=1)

    tk.Label(form_frame, text="Max C3:").grid(row=7, column=0)
    max_C3_entry = tk.Entry(form_frame)
    max_C3_entry.grid(row=7, column=1)

    # Label dan Entry untuk input rentang C4
    tk.Label(form_frame, text="Min C4:").grid(row=8, column=0)
    min_C4_entry = tk.Entry(form_frame)
    min_C4_entry.grid(row=8, column=1)

    tk.Label(form_frame, text="Max C4:").grid(row=9, column=0)
    max_C4_entry = tk.Entry(form_frame)
    max_C4_entry.grid(row=9, column=1)

    # Label dan Entry untuk input rentang C5
    tk.Label(form_frame, text="Min C5:").grid(row=10, column=0)
    min_C5_entry = tk.Entry(form_frame)
    min_C5_entry.grid(row=10, column=1)

    tk.Label(form_frame, text="Max C5:").grid(row=11, column=0)
    max_C5_entry = tk.Entry(form_frame)
    max_C5_entry.grid(row=11, column=1)

    # Tombol untuk submit data ke database
    submit_button = tk.Button(form_frame, text="Submit", command=add_reading)
    submit_button.grid(row=13, column=0, pady=(35, 5), columnspan=2)

    # Tombol untuk memperbarui data di database
    update_button = tk.Button(form_frame, text="Update", command=update_reading)
    update_button.grid(row=14, column=0, pady=5, columnspan=2)

    # Tombol untuk menghapus data dari database
    delete_button = tk.Button(form_frame, text="Delete", command=delete_reading)
    delete_button.grid(row=15, column=0, pady=5, columnspan=2)

    # Membuat tabel untuk menampilkan data dari database
    columns = ("ID", "Nama", "Min C1", "Max C1", "Min C2", "Max C2", "Min C3", "Max C3", "Min C4", "Max C4", "Min C5", "Max C5", "Time")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nama", text="Nama")
    tree.heading("Min C1", text="Min C1")
    tree.heading("Max C1", text="Max C1")
    tree.heading("Min C2", text="Min C2")
    tree.heading("Max C2", text="Max C2")
    tree.heading("Min C3", text="Min C3")
    tree.heading("Max C3", text="Max C3")
    tree.heading("Min C4", text="Min C4")
    tree.heading("Max C4", text="Max C4")
    tree.heading("Min C5", text="Min C5")
    tree.heading("Max C5", text="Max C5")
    tree.heading("Time", text="Time")
    
    for col in columns:
        tree.heading(col, text=col, anchor = "center")
        tree.column(col, width=100, minwidth=100, stretch=True, anchor="center")

    tree.pack(fill='both', expand=True, pady=20)

    # Mengisi tabel dengan data dari database saat pertama kali dijalankan
    get_readings()

    # Menjalankan GUI
    root.mainloop()

    # Menutup koneksi database setelah GUI ditutup
    cursor.close()
    db.close()


if __name__ == "__main__":
    form_tanah()
