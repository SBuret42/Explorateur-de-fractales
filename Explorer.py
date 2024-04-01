from PIL import Image
import time
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import keyboard
import numpy as np

# création de toutes les fenètres
def afficher_nouvelle_fenetre(message):
    fenetre.withdraw()  # Masque la fenêtre actuelle
    nouvelle_fenetre = Toplevel(fenetre)
    nouvelle_fenetre.title("Nouvelle Fenêtre")
    nouvelle_fenetre.geometry("720x555")  # Définir la même taille que la fenêtre principale
    Label(nouvelle_fenetre, text=message).pack(padx=20, pady=20)

def affiche_acceuil():
    cadre_pile.append(cadre_acceuil)  # Ajouter le cadre actuel à la pile
    afficher_cadre(cadre_acceuil)

def affiche_tuto():
    cadre_pile.append(cadre_tuto)  # Ajouter le cadre actuel à la pile
    afficher_cadre(cadre_tuto)
    
def affiche_biblio():
    cadre_pile.append(cadre_biblio)  # Ajouter le cadre actuel à la pile
    afficher_cadre(cadre_biblio)
    
def afficher_cadre(cadre):
    for c in [cadre_acceuil, cadre_tuto, cadre_biblio]:
        c.pack_forget()
    cadre.pack()


#valeurs de base
xmax = 2
xmin = -2
ymax = 1.3875
ymin = -1.387



#génération de la fenètre
fenetre = tk.Tk()

fenetre.title("L'exploreur de fractale")
fenetre.geometry("720x555")
fenetre.config(bg="#C2C2C2")
fenetre.iconbitmap("Explorer_image/logo.ico")
fenetre.minsize(720,555)
fenetre.maxsize(720,555)

cadre_acceuil = tk.Frame(fenetre, bg="#C2C2C2",heigh = 555,width=720)
cadre_acceuil.pack_propagate(False) 
cadre_tuto = tk.Frame(fenetre, bg="#C2C2C2",heigh = 555,width=720)
cadre_tuto.pack_propagate(False)
cadre_biblio = tk.Frame(fenetre, bg="#C2C2C2",heigh = 555,width=720)
cadre_biblio.pack_propagate(False) 

titre_biblio = tk.Label(cadre_biblio, text="Bbliothèque", font=("Consolas", 20), bg="#C2C2C2", fg="black")
soustitre_biblio = tk.Label(cadre_biblio, text="Vous cherchez un exemple de fractale ?", font=("Consolas", 15), bg="#C2C2C2", fg="black")
titre_biblio.pack()
soustitre_biblio.pack(pady=10)

titre_tuto = tk.Label(cadre_tuto, text="Guide des Touches", font=("Consolas", 20), bg="#C2C2C2", fg="black")
soustitre_tuto = tk.Label(cadre_tuto, text="Vous vous sentez un peux  perdu ?", font=("Consolas", 15), bg="#C2C2C2", fg="black")
titre_tuto.pack()
soustitre_tuto.pack(pady=10)

texte_tuto = tk.Label(cadre_tuto, text="z - aller vers le haut \ns - aller vers le bas \nq - aller à droite \nd - aller à gauche \n\nflèche du haut - zoom avant \nflèche du bas - zoom arrière \n\nm - renvoie les coordonnée de \n    où vous étes dans la fractale \n\nc - sauvegarde un PNG de ce que \n    vous voyez dans le dossier Explorer_image \n", font=("Consolas", 13), bg="#C2C2C2", fg="black")
texte_tuto.pack()

fin = tk.Label(cadre_tuto, text="Amusez vous !", font=("Consolas", 15), bg="#C2C2C2", fg="black")
fin.pack(pady=20)

titre_acceuil = tk.Label(cadre_acceuil, text="Bienvenue sur cet explorateur de fractales", font=("Consolas", 20), bg="#C2C2C2", fg="black")
soustitre_acceuil = tk.Label(cadre_acceuil, text="Choississez les paramètre de votre fractale", font=("Consolas", 15), bg="#C2C2C2", fg="black")
titre_acceuil.pack(pady=10)
soustitre_acceuil.place(x=130,y=50)

desc_liste_deroul_palette = tk.Label(cadre_acceuil, text="Choississez la palette de couleur que vous voulez utiliser", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc_liste_deroul_palette.place(x=15,y=100)
#création de la liste déroulante
liste_choix = ["Blanc - Jaune - Noir","Blanc - Noir","Noir - Rouge - Noir","Noir - Bleu - Noir"]
variable_palette = tk.StringVar()
variable_palette.set("Blanc - Noir")
liste_deroulante_palette = ttk.Combobox(cadre_acceuil, textvariable=variable_palette, values=liste_choix, state="readonly")
liste_deroulante_palette.place(x=15,y=125)
select = liste_deroulante_palette.get()

desc_liste_deroul_fractale = tk.Label(cadre_acceuil, text="Choississez la fractale que vous voulez voir", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc_liste_deroul_fractale.place(x=15,y=145)
#création de la liste déroulante
liste_choix = ["Julia","Mandelbrot"]
variable_fractal = tk.StringVar()
variable_fractal.set("Julia")
liste_deroulante_fractal = ttk.Combobox(cadre_acceuil, textvariable=variable_fractal, values=liste_choix, state="readonly")
liste_deroulante_fractal.place(x=15,y=170)

desc1_chmp_val_julia = tk.Label(cadre_acceuil, text="Si vous avez choisi de générer une fractale de Julia :", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc2_chmp_val_julia = tk.Label(cadre_acceuil, text="Choississez la valeur de la constante c (où laissez par defaut), sachant c est un complexe", font=("Consolas", 10), bg="#C2C2C2", fg="black")
desc1_chmp_val_julia.place(x=15,y=195)
desc2_chmp_val_julia.place(x=25,y=220)

variable_r = tk.StringVar()
variable_r.set("0.36")
chmp_str_c_r_julia = tk.Entry(cadre_acceuil, textvariable=variable_r, font=("Helvetica",12), bg="#ffffff", fg="black", width=5)
chmp_str_c_r_julia.place(x=40,y=245)
variable_i = tk.StringVar()
variable_i.set("0.36")
chmp_str_c_i_julia = tk.Entry(cadre_acceuil, textvariable=variable_i, font=("Helvetica",12), bg="#ffffff", fg="black", width=5)
chmp_str_c_i_julia.place(x=100,y=245)

desc_liste_deroul_resolution = tk.Label(cadre_acceuil, text="Choississez la résolution de l'exploreur", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc_liste_deroul_resolution.place(x=15,y=270)
#création de la liste déroulante
liste_choix = ["320x222","480x333","720x555"]
variable_resolution = tk.StringVar()
variable_resolution.set("320x222")
liste_deroulante_resolution = ttk.Combobox(cadre_acceuil, textvariable=variable_resolution, values=liste_choix, state="readonly")
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
    elif select == "Noir - Rouge - Noir":
        r, g, b = 0, 0, 0
        for j in range(0, 128):
            r = 0 + 2 * j
            palette.append((r, g, b))
        for j in range(128, 256):
            r = 255 - 2 * (j - 128)
            palette.append((r, g, b))
    elif select == "Noir - Bleu - Noir":
        r, g, b = 0, 0, 0
        for j in range(0, 128):
            b = 0 + 2 * j
            palette.append((r, g, b))
        for j in range(0, 128):
            b = 255 - 2 * j
            palette.append((r, g, b))
    else :
        palette = [[i,i,i] for i in range(255)]

def start():
    global img,chemin_image,canvas,choix_fract,compl_r,compl_i, réso_x, réso_y
    
    selection_palette()
    if liste_deroulante_fractal.get() == "Julia":
        choix_fract = 0
    if liste_deroulante_fractal.get() == "Mandelbrot":
        choix_fract = 1
    
    selection_reso()
    
    compl_r,compl_i = chmp_str_c_r_julia.get(),chmp_str_c_i_julia.get()
    
    fenetre.destroy()
    
    cadre_acceuil_explo = tk.Tk()
    cadre_acceuil_explo.iconbitmap("Explorer_image/logo.ico")
    cadre_acceuil_explo.title("Explorateur de fractale")
    
    # Remplacez le chemin du fichier par le chemin de votre image PNG
    chemin_image = "Explorer_image/Image.png"
    
    # Charge l'image
    img = PhotoImage(file=chemin_image)
    
    # Crée un widget Canvas pour afficher l'image
    canvas = tk.Canvas(cadre_acceuil_explo, width=réso_x, height=réso_y)
    canvas.pack()
    
    fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
    afficher_image()
    
    keyboard.hook(explorer)
    cadre_acceuil_explo.mainloop()

bouton_start_explo = tk.Button(cadre_acceuil, text="Commencer l'exploration", font=("Consolas",15), bg="white", fg="black", command = start)
bouton_start_explo.place(x=230,y=495)
    
def fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i, N_iteration = 100,nom_img='Explorer_image/Image.png'):
    global choix_fract,img
    
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
    img.save(nom_img)

def previsu():
    global palette, choix_fract,compl_r,compl_i, réso_x, réso_y, compl_r,compl_i
    réso_x, réso_y = 240,167
    selection_palette()
    if liste_deroulante_fractal.get() == "Julia":
        choix_fract = 0
    if liste_deroulante_fractal.get() == "Mandelbrot":
        choix_fract = 1
   
    compl_r,compl_i = chmp_str_c_r_julia.get(),chmp_str_c_i_julia.get()
    fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
    prévi = PhotoImage(file="Explorer_image/Image.png")
    label_image = tk.Label(cadre_acceuil, image=prévi)
    label_image.place(x=245,y=310)
    label_image.mainloop()

bouton_prévisualiser = tk.Button(cadre_acceuil, text="Prévisualiser", font=("Consolas",15), bg="white", fg="black", command = previsu)
bouton_prévisualiser.place(x=60,y=495)

def afficher_image():
    global img
    img = PhotoImage(file=chemin_image)
    image_explo = tk.Label(canvas, image=img)
    image_explo.place(y=0,x=0)

nbr_img = 0

def explorer(action):
    global xmax, xmin, ymax, ymin,img,nbr_img,réso_x, réso_y,compl_r,compl_i
    x = xmax - xmin
    y = ymax - ymin
    
    if keyboard.is_pressed('up'):#zoom avant
        xmax = xmax - (x/20)
        xmin = xmin - (x/20)*-1
        ymax = ymax - (y/20)
        ymin = ymin - (y/20)*-1
        fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
        afficher_image()      
    elif keyboard.is_pressed('down'):#zoom arrière
        xmax = xmax + (x/20)
        xmin = xmin + (x/20)*-1
        ymax = ymax + (y/20)
        ymin = ymin + (y/20)*-1
        fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
        afficher_image()
    elif keyboard.is_pressed('z'):
        ymax = ymax - (y/40)
        ymin = ymin - (y/40)
        fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
        afficher_image()
    elif keyboard.is_pressed('s'):
        ymax = ymax + (y/40)
        ymin = ymin + (y/40)
        fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
        afficher_image()
    elif keyboard.is_pressed('q'):
        xmax = xmax - (x/40)
        xmin = xmin - (x/40)
        fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
        afficher_image()
    elif keyboard.is_pressed('d'):
        xmax = xmax + (x/40)
        xmin = xmin + (x/40)
        fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i)
        afficher_image()
    elif keyboard.is_pressed('m'):
        print("xmax = ",xmax)
        print("xmin = ",xmin)
        print("ymax = ",ymax)
        print("ymin = ",ymin)
    elif keyboard.is_pressed('c'):
        print("Image enregistrée !")
        nbr_img +=1
        fractal_builder(xmax, xmin, ymax, ymin,réso_x, réso_y, palette, compl_r,compl_i,100,'Explorer_image/Image_saved'+str(nbr_img)+'.png')
        afficher_image()
        print(nbr_img)
        
# Affichage initial sur la page d'accueil
cadre_acceuil.pack()

# Création du menu
menubar = tk.Menu(fenetre)

# Ajout des commandes directement au menu principal
menubar.add_command(label="Acceuil", command=affiche_acceuil)
menubar.add_command(label="Guide des touches", command=affiche_tuto)
menubar.add_command(label="Bibliothèque", command=affiche_biblio)

# Configuration de la fenêtre avec la barre de menus
fenetre.config(menu=menubar)

# Initialisation de la pile des cadres
cadre_pile = [cadre_acceuil]

fenetre.mainloop()