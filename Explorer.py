from PIL import Image
import time
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import keyboard
import numpy as np


global xmax, xmin, ymax, ymin, réso_x, réso_y, r, g, b, palette #variable de où je suis dans la fractale
#valeurs de base
xmax = 2
xmin = -2
ymax = 1.3875
ymin = -1.387
réso_x = 320
réso_y = 222
palette = []

#génération de la fenètre
fenetre = tk.Tk()

fenetre.title("L'exploreur de fractale")
fenetre.geometry("720x555")
fenetre.config(bg="#C2C2C2")
fenetre.iconbitmap("Explorer_image/logo.ico")

titre_acceuil = tk.Label(fenetre, text="Bienvenue sur cet explorateur de fractales", font=("Consolas", 20), bg="#C2C2C2", fg="black")
soustitre_acceuil = tk.Label(fenetre, text="Choississez les paramètre de votre fractale", font=("Consolas", 15), bg="#C2C2C2", fg="black")
titre_acceuil.pack(pady=10)
soustitre_acceuil.place(x=130,y=50)

desc_liste_deroul_palette = tk.Label(fenetre, text="Choississez la palette de couleur que vous voulez utiliser", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc_liste_deroul_palette.place(x=15,y=100)
#création de la liste déroulante
liste_choix = ["Blanc - Jaune - Noir","Blanc - Noir"]
variable_palette = tk.StringVar()
variable_palette.set("Blanc - Noir")
liste_deroulante_palette = ttk.Combobox(fenetre, textvariable=variable_palette, values=liste_choix)
liste_deroulante_palette.place(x=15,y=125)
select = liste_deroulante_palette.get()

desc_liste_deroul_fractale = tk.Label(fenetre, text="Choississez la fractale que vous voulez voir", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc_liste_deroul_fractale.place(x=15,y=145)
#création de la liste déroulante
liste_choix = ["Julia","Mandelbrot"]
variable_fractal = tk.StringVar()
variable_fractal.set("Julia")
liste_deroulante_fractal = ttk.Combobox(fenetre, textvariable=variable_fractal, values=liste_choix)
liste_deroulante_fractal.place(x=15,y=170)

desc1_chmp_val_julia = tk.Label(fenetre, text="Si vous avez choisi de générer une fractale de Julia :", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc2_chmp_val_julia = tk.Label(fenetre, text="Choississez la valeur de la constante c (où laissez par defaut), sachant c est un complexe", font=("Consolas", 10), bg="#C2C2C2", fg="black")
desc1_chmp_val_julia.place(x=15,y=195)
desc2_chmp_val_julia.place(x=25,y=220)

variable_r = tk.StringVar()
variable_r.set("0.36")
chmp_str_c_r_julia = tk.Entry(fenetre, textvariable=variable_r, font=("Helvetica",12), bg="#ffffff", fg="black", width=5)
chmp_str_c_r_julia.place(x=40,y=245)
variable_i = tk.StringVar()
variable_i.set("0.36")
chmp_str_c_i_julia = tk.Entry(fenetre, textvariable=variable_i, font=("Helvetica",12), bg="#ffffff", fg="black", width=5)
chmp_str_c_i_julia.place(x=100,y=245)

desc_liste_deroul_resolution = tk.Label(fenetre, text="Choississez la résolution de l'exploreur", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc_liste_deroul_resolution.place(x=15,y=270)
#création de la liste déroulante
liste_choix = ["320x222","480x333","720x555"]
variable_resolution = tk.StringVar()
variable_resolution.set("320x222")
liste_deroulante_resolution = ttk.Combobox(fenetre, textvariable=variable_resolution, values=liste_choix)
liste_deroulante_resolution.place(x=15,y=295)

def selection_reso():
    global réso_x,réso_y
    if liste_deroulante_resolution.get() == "320x222":
        réso_x = 320
        réso_y = 222
    if liste_deroulante_resolution.get() == "480x333":
        réso_x = 480
        réso_y = 333
    if liste_deroulante_resolution.get() == "720x555":
        réso_x = 720
        réso_y = 555

def selection_palette():
    global palette
    palette = []
    select = liste_deroulante_palette.get()
    if select == "Blanc - Jaune - Noir":
        r, g, b = 255, 255, 255
        for j in range(0, 128):
            b = 255 - 2 * j
            palette.append((r, g, b))
        for j in range(128, 256):
            r = 255 - 2 * (j - 128)
            g = 255 - 2 * (j - 128)
            palette.append((r, g, b))
    else :
        palette = [[i,i,i] for i in range(255)]

def start():
    global img,chemin_image,canvas,choix_fract,compl_r,compl_i, réso_x, réso_y
    réso_x, réso_y = 320,222
    
    selection_palette()
    if liste_deroulante_fractal.get() == "Julia":
        choix_fract = 0
    if liste_deroulante_fractal.get() == "Mandelbrot":
        choix_fract = 1
    
    selection_reso()
    
    compl_r,compl_i = chmp_str_c_r_julia.get(),chmp_str_c_i_julia.get()
    
    fenetre.destroy()
    
    fenetre_explo = tk.Tk()
    fenetre_explo.title("Affichage d'une Image")
    
    # Remplacez le chemin du fichier par le chemin de votre image PNG
    chemin_image = "Explorer_image/Image.png"
    
    # Charge l'image
    img = PhotoImage(file=chemin_image)
    
    # Crée un widget Canvas pour afficher l'image
    canvas = tk.Canvas(fenetre_explo, width=réso_x, height=réso_y)
    canvas.pack()
    
    fenetre_explo.mainloop()

bouton_start_explo = tk.Button(fenetre, text="Commencer l'exploration", font=("Consolas",15), bg="white", fg="black", command = start)
bouton_start_explo.place(x=230,y=505)
    
def fractal_builder(N_iteration = 100):
    global xmax, xmin, ymax, ymin, réso_x, réso_y, r, g, b, palette, choix_fract,compl_r,compl_i
    
    palette = np.array(palette, dtype=np.uint8)

    # Créer une grille de coordonnées complexes
    x = np.linspace(xmin, xmax, réso_x)
    y = np.linspace(ymin, ymax, réso_y)
    X, Y = np.meshgrid(x, y)
    Z = X + 1J * Y

    # Initialiser une matrice d'indices pour la palette
    indices_matrix = np.zeros((réso_y, réso_x), dtype=int)

    for i in range(N_iteration):
        # Mettre à jour les pixels
        mask = np.logical_and(i < N_iteration, np.abs(Z) < 2)
        indices_matrix[mask] = np.round(255 * i / N_iteration).astype(int)

        # Mettre à jour Z pour les pixels actifs
        if choix_fract == 1:
            Z[mask] = Z[mask] ** 2 + X[mask] + 1J * Y[mask]
        if choix_fract == 0:
            c = complex(float(compl_r), float(compl_i))
            Z[mask] = Z[mask] ** 2 + c

    # Créer une image à partir de la matrice d'indices
    img_array = palette[indices_matrix]

    # Créer une image PIL à partir de l'array
    img = Image.fromarray(img_array, 'RGB')

    # Sauvegarder l'image
    img.save('Explorer_image/Image.png')    

def previsu():
    global palette, choix_fract,compl_r,compl_i, réso_x, réso_y
    réso_x, réso_y = 240,167
    selection_palette()
    if liste_deroulante_fractal.get() == "Julia":
        choix_fract = 0
    if liste_deroulante_fractal.get() == "Mandelbrot":
        choix_fract = 1
   
    compl_r,compl_i = chmp_str_c_r_julia.get(),chmp_str_c_i_julia.get()
    fractal_builder()
    prévi = PhotoImage(file="Explorer_image/Image.png")
    label_image = tk.Label(fenetre, image=prévi)
    label_image.place(x=245,y=310)
    label_image.mainloop()

bouton_prévisualiser = tk.Button(fenetre, text="Prévisualiser", font=("Consolas",15), bg="white", fg="black", command = previsu)
bouton_prévisualiser.place(x=60,y=505)

def afficher_image():
    global img
    img = PhotoImage(file=chemin_image)
    # Affiche l'image sur le Canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    
def explorer(action):
    global xmax, xmin, ymax, ymin
    x = xmax - xmin
    y = ymax - ymin
    
    if keyboard.is_pressed('enter'):#lancement
        fractal_builder()
        afficher_image()
    elif keyboard.is_pressed('up'):#zoom avant
        xmax = xmax - (x/20)
        xmin = xmin - (x/20)*-1
        ymax = ymax - (y/20)
        ymin = ymin - (y/20)*-1
        fractal_builder()
        afficher_image()      
    elif keyboard.is_pressed('down'):#zoom arrière
        xmax = xmax + (x/20)
        xmin = xmin + (x/20)*-1
        ymax = ymax + (y/20)
        ymin = ymin + (y/20)*-1
        fractal_builder()
        afficher_image()
    elif keyboard.is_pressed('z'):
        ymax = ymax - (y/40)
        ymin = ymin - (y/40)
        fractal_builder()
        afficher_image()
    elif keyboard.is_pressed('s'):
        ymax = ymax + (y/40)
        ymin = ymin + (y/40)
        fractal_builder()
        afficher_image()
    elif keyboard.is_pressed('q'):
        xmax = xmax - (x/40)
        xmin = xmin - (x/40)
        fractal_builder()
        afficher_image()
    elif keyboard.is_pressed('d'):
        xmax = xmax + (x/40)
        xmin = xmin + (x/40)
        fractal_builder()
        afficher_image()
    
 

# Attachez la fonction de gestion des événements
keyboard.hook(explorer)
fenetre.mainloop()
# Gardez le script en cours d'exécution
keyboard.wait('esc')  # Attend jusqu'à ce que la touche Échap soit enfoncée