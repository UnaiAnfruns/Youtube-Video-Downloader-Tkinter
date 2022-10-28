from tkinter import *
from pytube import YouTube
from tkinter import messagebox
root = Tk()
root.geometry('662x476')
root.overrideredirect(1)
root.resizable(False, False)
root.wm_attributes("-transparentcolor", "grey")

def Descargar_fun():
    buscar_video()
    try:
        url = campo_de_texto.get("1.0", "end-1c")
        opcion = Opcion_Elegida.get("1.0", "end-1c")
        yt = YouTube(url)

        print(opcion)
        if int(opcion) == 1:
            #MP3
            print("Se va a descargar en MP3")
            ys = yt.streams.filter(only_audio=True).all()
            x = (ys[0])
            x.download()
        if int(opcion) == 2:
            print("Se va a descargar en MAX RES")
            ys = yt.streams.get_highest_resolution()
            ys.download()
        if int(opcion) == 3:
            print("Se va a descargar en LOW RES")
            ys = yt.streams.get_lowest_resolution()
            print(ys)
            ys.download()
        messagebox.showinfo(message="Completado correctamente", title="Video_Dowloader_By_AINS")
    except:
        Error.config(text=" URL NO VALIDA")

def solo_audio():
    print("Se ha ejectuado solo audio")
    SoloAudio_hover.place(x=68, y=197)
    CalidadMaxima_hover.place(x=-500, y=324)
    CalidadBaja_hover.place(x=-568, y=261)
    Opcion_Elegida.delete(1.0,"end")
    Opcion_Elegida.insert(1.0, "1")

def calidad_maxima():
    print("Se ha ejectuado calidad maxima")
    CalidadMaxima_hover.place(x=68,y=324)
    SoloAudio_hover.place(x=-968, y=197)
    CalidadBaja_hover.place(x=-568, y=261)
    Opcion_Elegida.delete(1.0,"end")
    Opcion_Elegida.insert(1.0, "2")

def calidad_minima():
    print("Se ha ejectuado calidad minima")
    CalidadBaja_hover.place(x=68,y=261)
    CalidadMaxima_hover.place(x=-500, y=324)
    SoloAudio_hover.place(x=-968, y=197)
    Opcion_Elegida.delete(1.0,"end")
    Opcion_Elegida.insert(1.0, "3")

def buscar_video():
    try:
        url=campo_de_texto.get("1.0","end-1c")
        test = Opcion_Elegida.get("1.0","end-1c")
        yt = YouTube(url)
        print(test)
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length)
        print(yt.thumbnail_url)
        print(yt.author)
        Minutos = str(yt.length/60)
        Minutos = Minutos.replace(" ","")
        y = 1
        Titulo = yt.title
        Titulo = Titulo.replace(" ","_")
        Titulo_nombre = ""
        for x in Titulo:
            if y < 33:
                Titulo_nombre = Titulo_nombre + x
                y += 1

        y = 1
        Minutos_Formato = ""
        for xy in Minutos:
            if y < 8:
                Minutos_Formato = Minutos_Formato + xy
                y += 1

        print(Minutos_Formato)

        Nombre_video.config(text="Nombre del video: \n{}".format(str(Titulo_nombre)))
        Visitas_video.config(text="  Vistias: {}".format(yt.views))
        Segundos_video.config(text=" Minutos del video: {}".format(str(Minutos_Formato)))
        Autor.config(text=" Autor del video: {}".format(yt.author))

    except:
        Error.config(text=" URL NO VALIDA")
def acabar_app():
    root.destroy()

def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

frame_photo = PhotoImage(file='./img/APP.png')
frame_label = Label(root,border=0,bg='grey',image=frame_photo)
frame_label.pack(fill=BOTH,expand=True)
frame_label.bind("<B1-Motion>", move_app)

Panel_Derecho_img = PhotoImage(file='./img/Deco(3).png')
Panel_Derecho = Label(root, image=Panel_Derecho_img,border=0,bg='#c86c6c')
Panel_Derecho.place(x=330,y=52)

Descargar_img = PhotoImage(file="./img/Descargar.png")
Descargar = Button(root, image=Descargar_img,border=0,bg="white",command=lambda : Descargar_fun())
Descargar.place(x=68,y=400)


UrlBuscar_img = PhotoImage(file="./img/URL_VIDEO.png")
UrlBuscar = Label(root, image=UrlBuscar_img,border=0,bg="white")
UrlBuscar.place(x=54,y=98.51)

CalidadBaja_img = PhotoImage(file="./img/CaidadBaja.png")
CalidadBaja = Button(root, image=CalidadBaja_img,border=0,bg="white",command=lambda estado_audio ="1": calidad_minima())
CalidadBaja.place(x=68,y=261)


SoloAudio_img = PhotoImage(file="./img/SoloAudio.png")
SoloAudio = Button(root, image=SoloAudio_img,border=0,bg="white",command=lambda estado_audio ="1": solo_audio())
SoloAudio.place(x=68,y=197)

CalidadMaxima_img = PhotoImage(file="./img/CalidadMaxima.png")
CalidadMaxima = Button(root, image=CalidadMaxima_img,border=0,bg="white",command=lambda estado_audio ="1": calidad_maxima())
CalidadMaxima.place(x=68,y=324)

Salirimg = PhotoImage(file='./img/Cerrar.png')
Salir = Button(root, image=Salirimg,border=0,bg='#c66868', command= lambda :(acabar_app()))
Salir.place(x=599,y=21)



#####
SoloAudio_img_2 = PhotoImage(file="./img/SoloAudio(1).png")
SoloAudio_hover = Button(root, image=SoloAudio_img_2,border=0,bg="white",command=lambda estado = 1 : solo_audio())

CalidadMaxima_img_2 = PhotoImage(file="./img/CalidadMaxima(1).png")
CalidadMaxima_hover = Button(root, image=CalidadMaxima_img_2,border=0,bg="white",command=lambda estado = 2: calidad_maxima())

CalidadBaja_img_2 = PhotoImage(file="./img/CaidadBaja(1).png")
CalidadBaja_hover = Button(root, image=CalidadBaja_img_2,border=0,bg="white",command=lambda estado = 3: calidad_minima())

#####

#Campo de texto
campo_de_texto = Text(root, height=8)
campo_de_texto.config(border=0,pady=5)
campo_de_texto.place(x=59, y=119.12,width=213,height=29)

Lupaimg = PhotoImage(file='./img/lupa.png')
Lupa = Button(root, image=Lupaimg,border=0,bg='white', command= lambda :(buscar_video()))
Lupa.place(x=279,y=124)


Nombre_video = Label(root, text="")
Nombre_video.config(font=("Arial", 10),border=0,fg="white",bg="#c86c6c")
Nombre_video.place(x=340, y=230)

Visitas_video = Label(root, text="")
Visitas_video.config(font=("Arial", 10),border=0,fg="white",bg="#c86c6c")
Visitas_video.place(x=335, y=280)

Segundos_video = Label(root, text="")
Segundos_video.config(font=("Arial", 10),border=0,fg="white",bg="#c86c6c")
Segundos_video.place(x=340, y=330)

Autor = Label(root, text="")
Autor.config(font=("Arial", 10),border=0,fg="white",bg="#c86c6c")
Autor.place(x=340, y=380)

Error = Label(root, text="")
Error.config(font=("Arial", 8),border=0,fg="red",bg="white")
Error.place(x=55, y=155)

Boton_Elegido = Text(root, height=8)
Boton_Elegido.config(border=0,pady=5)

Opcion_Elegida = Text(root, height=8)
Opcion_Elegida.config(border=0,pady=5)


root.mainloop()
