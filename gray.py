import tkinter as tk
def binary_to_gray():
    n=entrada1.get()
    """Convertir código binario a código gris y devolverlo."""
    n = int(n, 2) # convertirlo en int
    n ^= (n >> 1)
 
    # bin (n) devuelve la representación binaria de n con un prefijo '0b'
    # la operación de rebanada es eliminar el prefijo
    return var.set(bin(n)[2:])
ventana=tk.Tk()
ventana.title('Binario a Gray')
ventana.geometry('380x200')
ventana.configure(background='green')
var=tk.StringVar()


el=tk.Label(ventana,text="Número Binario",bg="blue",fg="white")
el.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)

entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

boton=tk.Button(ventana,text="Convertir",fg="blue",command=binary_to_gray)
boton.pack(side=tk.TOP)

res=tk.Label(ventana,bg="blue",fg="white",textvariable=var,padx=5,pady=5,width=50)
res.pack()
ventana.mainloop()

