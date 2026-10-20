import tkinter as tk
import tkinter.messagebox 

root = tk.Tk()

label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan")
label.pack()



L1 = tk.Label(root, text="1. Nilai Mata Pelajaran")
L1.pack()
E1 = tk.Entry(root, bd=5)
E1.pack()
L2 = tk.Label(root, text="2. Nilai Mata Pelajaran")
L2.pack()
E2 = tk.Entry(root, bd=5)
E2.pack()
L3 = tk.Label(root, text="3. Nilai Mata Pelajaran")
L3.pack()
E3 = tk.Entry(root, bd=5)
E3.pack()
L4 = tk.Label(root, text="4. Nilai Mata Pelajaran")
L4.pack()
E4 = tk.Entry(root, bd=5)
E4.pack()
L5 = tk.Label(root, text="5. Nilai Mata Pelajaran")
L5.pack()
E5 = tk.Entry(root, bd=5)
E5.pack()
L6 = tk.Label(root, text="6. Nilai Mata Pelajaran")
L6.pack()
E6 = tk.Entry(root, bd=5)
E6.pack()
L7 = tk.Label(root, text="7. Nilai Mata Pelajaran")
L7.pack()
E7 = tk.Entry(root, bd=5)
E7.pack()
L8 = tk.Label(root, text="8. Nilai Mata Pelajaran")
L8.pack()
E8 = tk.Entry(root, bd=5)
E8.pack()
L9 = tk.Label(root, text="9. Nilai Mata Pelajaran")
L9.pack()
E9 = tk.Entry(root, bd=5)
E9.pack()
L10 = tk.Label(root, text="10. Nilai Mata Pelajaran")
L10.pack()
E10 = tk.Entry(root, bd=5)
E10.pack()


def hasilPrediksi(): 
    tk.messagebox.showinfo( "Hello Python", "Teknologi Informasi") 
B = tk.Button(root, text ="Hasil Prediksi", command = hasilPrediksi) 
B.pack() 




root.mainloop()