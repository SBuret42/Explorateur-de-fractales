from PIL import Image, ImageTk
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

def image_biblio(image,x,y):
    img = PhotoImage(file=image)
    image_frame = tk.Label(cadre_biblio, image=img)
    image_frame.image = img
    image_frame.place(x=x,y=y)
    cadre_biblio.update() 
    
image_biblio("Bibliotheque_image/1.png",100,10)

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
liste_choix = ["Blanc - Jaune - Noir","Blanc - Noir","Noir - Bleu - Noir","Blanc - Orange - Noir","Arc-en-ciel", "Noir - Rouge - Noir"]
variable_palette = tk.StringVar()
variable_palette.set("Blanc - Noir")
liste_deroulante_palette = ttk.Combobox(cadre_acceuil, textvariable=variable_palette, values=liste_choix)
liste_deroulante_palette.place(x=15,y=125)
select = liste_deroulante_palette.get()

desc_liste_deroul_fractale = tk.Label(cadre_acceuil, text="Choississez la fractale que vous voulez voir", font=("Consolas", 12), bg="#C2C2C2", fg="black")
desc_liste_deroul_fractale.place(x=15,y=145)
#création de la liste déroulante
liste_choix = ["Julia","Mandelbrot"]
variable_fractal = tk.StringVar()
variable_fractal.set("Julia")
liste_deroulante_fractal = ttk.Combobox(cadre_acceuil, textvariable=variable_fractal, values=liste_choix)
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
liste_deroulante_resolution = ttk.Combobox(cadre_acceuil, textvariable=variable_resolution, values=liste_choix)
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
    elif select == "Noir - Bleu - Noir":
        r,g,b=0,0,0
        for i in range(0,64):
            g=0+i
            b=0+i*2
            palette.append([r,g,b])
        for i in range(0,64):
            g=64+i
            b=128+i*2
            palette.append([r,g,b])
        for i in range(0,64):
            r=0+i
            palette.append([r,g,b])
        for i in range(0,64):
            g=128+i*2
            r=64+i*3
            palette.append([r,g,b])
    elif select == "Blanc - Orange - Noir":
        r,g,b=240,240,240
        for i in range(0,64):
            r=240+i*(1/4)
            g=240-i*(1/4)
            b=240-i*(7/4)
            palette.append([r,g,b])
        for i in range(0,64):
            g=224-i*(3/2)
            b=128-i
            palette.append([r,g,b])
        for i in range(0,64):
            g=128-i*(1/2)
            palette.append([r,g,b])
        for i in range(0,64):
            b=64-i
            g=64-i
            r=255-i*4
            palette.append([r,g,b])
    elif select == "Arc-en-ciel":
        r, g, b = 255,255,255
        for j in range(0, 32):
            b = 255 - 8 * j
            g = 255 - 8 * j
            palette.append((r, g, b))
        for j in range(0, 32):
            g = 0 + 8 * j
            palette.append((r, g, b))
        for j in range(0, 32):
            r = 255 - 4 * j
            palette.append((r, g, b))
        for j in range(0, 32):
            r = 128 - 4 * j
            palette.append((r, g, b))
        for j in range(0, 32):
            b = 0 + 6 * j
            palette.append((r, g, b))
        for j in range(0, 32):
            r = 0 + 2 * j
            b = 192 + 2 * j
            palette.append((r, g, b))
        for j in range(0, 32):
            r = 64 + 2 * j
            palette.append((r, g, b))
        for j in range(0, 32):
            r = 128 - 4 * j
            b = 255 - 8 * j
            g = 255 - 8 * j
            palette.append((r, g, b))
    elif select == "Noir - Rouge - Noir":
        r, g, b = 0, 0, 0
        for j in range(0, 85):
            r = 0 + (j/2)
            palette.append((r, g, b))
        for j in range(0, 85):
            r = 64 + j * 3/2
            palette.append((r, g, b))
        for j in range(0, 85):
            r = 255 - j * 3
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
    cadre_acceuil_explo.title("Affichage d'une Image")
    
    # Remplacez le chemin du fichier par le chemin de votre image PNG
    chemin_image = "Explorer_image/Image.png"
    
    # Charge l'image
    img = PhotoImage(file=chemin_image)
    
    # Crée un widget Canvas pour afficher l'image
    canvas = tk.Canvas(cadre_acceuil_explo, width=720, height=555)
    canvas.pack()
    
    fractal_builder()
    afficher_image()
    
    cadre_acceuil_explo.mainloop()

bouton_start_explo = tk.Button(cadre_acceuil, text="Commencer l'exploration", font=("Consolas",15), bg="white", fg="black", command = start)
bouton_start_explo.place(x=230,y=495)
    
def fractal_builder(N_iteration = 100,nom_img='Explorer_image/Image.png',resox=320,resoy=222):
    global xmax, xmin, ymax, ymin, r, g, b, palette, choix_fract,compl_r,compl_i,img
    
    palette = np.array(palette, dtype=np.uint8)

    # Créer une grille de coordonnées complexes
    x = np.linspace(xmin, xmax, resox)
    y = np.linspace(ymin, ymax, resoy)
    X, Y = np.meshgrid(x, y)
    Z = X + 1J * Y

    # Initialiser une matrice d'indices pour la palette
    indices_matrix = np.zeros((resoy, resox), dtype=int)

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
    global palette, choix_fract,compl_r,compl_i
    selection_palette()
    if liste_deroulante_fractal.get() == "Julia":
        choix_fract = 0
    if liste_deroulante_fractal.get() == "Mandelbrot":
        choix_fract = 1
   
    compl_r,compl_i = chmp_str_c_r_julia.get(),chmp_str_c_i_julia.get()
    fractal_builder(100,'Explorer_image/Image.png',240,167)
    prévi = PhotoImage(file="Explorer_image/Image.png")
    label_image = tk.Label(cadre_acceuil, image=prévi)
    label_image.place(x=245,y=310)
    label_image.mainloop()

bouton_prévisualiser = tk.Button(cadre_acceuil, text="Prévisualiser", font=("Consolas",15), bg="white", fg="black", command = previsu)
bouton_prévisualiser.place(x=60,y=495)

def afficher_image():
    global chemin_image, réso_x, réso_y, canvas
    
    # Charge l'image et redimensionne-la
    img = Image.open(chemin_image)
    img_redim = img.resize((720, 555))
    
    # Convertit l'image redimensionnée en un objet PhotoImage
    photo = ImageTk.PhotoImage(img_redim)
    
    # Affiche l'image sur le Canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    
    # Garde une référence à l'objet PhotoImage pour éviter que Python ne le supprime
    canvas.image = photo

nbr_img = 0

def explorer(action):
    global xmax, xmin, ymax, ymin,img,nbr_img
    x = xmax - xmin
    y = ymax - ymin
    
    if keyboard.is_pressed('up'):#zoom avant
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
    elif keyboard.is_pressed('m'):
        print("xmax = ",xmax)
        print("xmin = ",xmin)
        print("ymax = ",ymax)
        print("ymin = ",ymin)
    elif keyboard.is_pressed('c'):
        print("Image enregistrée !")
        nbr_img +=1
        fractal_builder(100,'Explorer_image/Image_saved'+str(nbr_img)+'.png',1040,721)
        afficher_image()
        print(nbr_img)
        
# Affichage initial sur la page d'accueil
cadre_acceuil.pack()

# Création du menu
menubar = tk.Menu(fenetre)

# Ajout des commandes directement au menu principal
menubar.add_command(label="Acceuil", command=affiche_acceuil)
menubar.add_command(label="Bibliothèque", command=affiche_biblio)
menubar.add_command(label="Guide des touches", command=affiche_tuto)

# Configuration de la fenêtre avec la barre de menus
fenetre.config(menu=menubar)

# Initialisation de la pile des cadres
cadre_pile = [cadre_acceuil]

# Attachez la fonction de gestion des événements
keyboard.hook(explorer)
fenetre.mainloop()
# Gardez le script en cours d'exécution
keyboard.wait('esc')  # Attend jusqu'à ce que la touche Échap soit enfoncée
