import time
from tkinter import *
from functools import partial
from random import *
from PIL import *
from pygame import *

# Début Modele
# Variable Global
global porte_avion_image, porte_avion, croiseur_image, croiseur, contretorpi1_image, contretorpi1, contretorpi2_image, contretorpi2, torpi1, torpi1_image, image_fondecran, image_canva, image_jouer, jouer_tButton, image_jouer, image_facile, facile_tButton, levelia, root, all_explosion, explosion_image, rate_image, all_rate, liste_img_ordi, place_image_bateau_ordi, nbr_touche_bateau_4, nbr_touche_bateau_5, nbr_touche_bateau_3_1, nbr_touche_bateau_3_2, nbr_touche_bateau_2, nbr_tir_ordi, nbr_tir_joueur, nbr_bateaux_coule_ordi, nbr_bateaux_coule_joueur, bateau_couler_par_ordi

nbr_tir_ordi = 0
nbr_tir_joueur = 0
nbr_bateaux_coule_ordi = 0
nbr_bateaux_coule_joueur = 0

bateau_couler_par_ordi = [0, 0, 0, 0, 0]
place_image_bateau_ordi = []
levelia = 0
posx = 0
posy = 0
bateauxtouchejoueur = 0
bateauxtoucheordi = 0
SPACE = 60
PLATEAU_JOUEUR1 = [[0] * 10 for _ in range(10)]
PLATEAU_ORDI = [[0] * 10 for _ in range(10)]
old = [0, 0]
position_bateau_1 = 1
rate_image = []
all_rate = []
all_explosion = []
explosion_image = []
position_bateau_2 = 1
position_bateau_3 = 1
position_bateau_4 = 1
position_bateau_5 = 1

ALPHABET = "ABCDEFGHIJ"
nbr_touche_bateau_4 = 0
nbr_touche_bateau_5 = 0
nbr_touche_bateau_3_1 = 0
nbr_touche_bateau_3_2 = 0
nbr_touche_bateau_2 = 0


# FIN : Variable Global
# Relancer le jeu
def reset(canva_full_screen, event):
    global root, place_image_bateau_ordi, levelia, posx, posy, bateauxtouchejoueur, bateauxtoucheordi, SPACE, PLATEAU_JOUEUR1, PLATEAU_ORDI, old, position_bateau_1, rate_image, all_rate, all_explosion, explosion_image, position_bateau_2, position_bateau_3, position_bateau_4, position_bateau_5, ALPHABET, nbr_touche_bateau_4, nbr_touche_bateau_5, nbr_touche_bateau_3_1, nbr_touche_bateau_3_2, nbr_touche_bateau_2
    root.destroy()
    place_image_bateau_ordi = []
    levelia = 0
    posx = 0
    posy = 0
    bateauxtouchejoueur = 0
    bateauxtoucheordi = 0
    SPACE = 60
    PLATEAU_JOUEUR1 = [[0] * 10 for _ in range(10)]
    PLATEAU_ORDI = [[0] * 10 for _ in range(10)]
    old = [0, 0]
    position_bateau_1 = 1
    rate_image = []
    all_rate = []
    all_explosion = []
    explosion_image = []
    position_bateau_2 = 1
    position_bateau_3 = 1
    position_bateau_4 = 1
    position_bateau_5 = 1

    nbr_touche_bateau_4 = 0
    nbr_touche_bateau_5 = 0
    nbr_touche_bateau_3_1 = 0
    nbr_touche_bateau_3_2 = 0
    nbr_touche_bateau_2 = 0
    main()


# Fin Relancer le jeu


# Quitter le jeu
def destroy(a, event):
    global root
    root.destroy()


# Fin Quitter le jeu


# Verification de la position des bateaux du joueur, collision, bateaux non positionné.
def check_boat_place(canva_full_screen, canva_all_boat, teste_placement, Start_the_game):
    global stat_joueur, stat_ordi, Tour_player
    invalid = False
    bateaux_place = True
    global PLATEAU_JOUEUR1
    global PLATEAU_ORDI
    for element in canva_all_boat:
        x1 = int(canva_full_screen.coords(element)[0] // SPACE)
        x2 = int(canva_full_screen.coords(element)[2] // SPACE)
        y1 = int(canva_full_screen.coords(element)[1] // SPACE)
        y2 = int(canva_full_screen.coords(element)[3] // SPACE)

        if (0 <= x1 <= 10 and 0 <= x2 <= 10) and (0 <= y1 <= 10 and 0 <= y2 <= 10):
            for i in range(x1, x2):
                for y in range(y1, y2):
                    if PLATEAU_JOUEUR1[y][i] == 0:
                        PLATEAU_JOUEUR1[y][i] = element
                    else:
                        invalid = True
        else:
            bateaux_place = False
    if bateaux_place:
        if (invalid):
            canva_full_screen.itemconfig(teste_placement, text="Vos bateaux s'entre-choque, veuillez les déplacer.")

            PLATEAU_JOUEUR1 = [[0] * 10 for _ in range(10)]
        else:

            canva_full_screen.unbind("<Button-1>")
            canva_full_screen.unbind("<Button-3>")
            canva_full_screen.unbind("<Button-2>")
            canva_full_screen.unbind("<B1-Motion>")
            canva_full_screen.unbind("<ButtonRelease-1>")
            canva_full_screen.delete(teste_placement)
            Start_the_game.destroy()
            affichage_plateau_ordinateur(canva_full_screen)
            creation_bateau_ordi(canva_full_screen)
            stat_joueur = canva_full_screen.create_text(40, 700, text="Nombre de tir : " + str(
                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                                        font=('Helvetica 20 bold'), fill="white", anchor="nw")
            stat_ordi = canva_full_screen.create_text(1100, 700, text="Nombre de tir : " + str(
                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                                      font=('Helvetica 20 bold'), fill="white", anchor="nw")
            Tour_player = canva_full_screen.create_text(650, 700, text="Tour : Joueur",
                                                        font=('Helvetica 20 bold'), fill="white", anchor="nw")
            canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))



    else:
        PLATEAU_JOUEUR1 = [[0] * 10 for _ in range(10)]

        canva_full_screen.itemconfig(teste_placement, text="Veuillez placer tous les bateaux sur la grille.")


# FIN : Verification de la position des bateaux du joueur, collision, bateaux non positionné.

# Fin Modele


# Début IHM
# S'affiche lorsque qu'on clique sur le bouton jouer.
def affichage_plateau_joueur(canva_full_screen):
    global plateau, plateau_joueur

    plateau = PhotoImage(file='plateau.gif')

    plateau_joueur = canva_full_screen.create_image(340,
                                                    340,
                                                    image=plateau)

    label_joueur = canva_full_screen.create_text(310, 680, text="JOUEUR", font=('Helvetica 20 bold'), fill="white")

    for i in range(1, len(PLATEAU_JOUEUR1) + 1):
        canva_full_screen.create_text(15 + i * SPACE, 15, text=str(i), font=('Helvetica 15 bold'), fill="white")
        canva_full_screen.create_text(15, i * SPACE, text=ALPHABET[i - 1], font=('Helvetica 15 bold'), fill="white")

    for i in range(len(PLATEAU_JOUEUR1)):
        for j in range(len(PLATEAU_JOUEUR1[0])):
            carre_grille_joueur = canva_full_screen.create_rectangle(40 + SPACE * i, 40 + SPACE * j,
                                                                     40 + SPACE * (i + 1), 40 + SPACE * (j + 1),
                                                                     fill="",
                                                                     outline="black")
            canva_full_screen.tag_raise(carre_grille_joueur)


# FIN : S'affiche lorsque qu'on clique sur le bouton jouer.

# S'affiche après que les bateaux du joueurs soit placé correctement.
def affichage_plateau_ordinateur(canva_full_screen):
    global plateau1, plateau_ordi2
    plateau1 = PhotoImage(file='plateau.gif')

    plateau_ordi2 = canva_full_screen.create_image(750 + 300,
                                                   340,
                                                   image=plateau)
    label_ordi = canva_full_screen.create_text(1050, 680, text="ORDINATEUR", font=('Helvetica 20 bold'), fill="white")
    for i in range(1, len(PLATEAU_ORDI) + 1):
        canva_full_screen.create_text(725 + i * SPACE, 15, text=str(i), font=('Helvetica 15 bold'), fill="white")
        canva_full_screen.create_text(735, i * SPACE, text=ALPHABET[i - 1], font=('Helvetica 15 bold'), fill="white")

    for i in range(len(PLATEAU_ORDI)):
        for j in range(len(PLATEAU_JOUEUR1[0])):
            carre_grille_joueur = canva_full_screen.create_rectangle(750 + SPACE * i, 40 + SPACE * j,
                                                                     750 + SPACE * (i + 1), 40 + 60 + SPACE * j,
                                                                     fill="",
                                                                     outline="black")


# FIN : S'affiche après que les bateaux du joueurs soit placé correctement.

# Creation des bateaux joueurs
def creation_bateau(canva_full_screen):
    teste_placement = Label(canva_full_screen, text="Veuillez placer vos bateaux", fg="black", bg="grey")
    teste_placement = canva_full_screen.create_text(780, 680, text="Veuillez placer vos bateaux",
                                                    font=('Helvetica 15 bold'), fill="white")

    global porte_avion_image, porte_avion, croiseur_image, croiseur, contretorpi1_image, contretorpi1, contretorpi2_image, contretorpi2, torpi1, torpi1_image
    canva_all_boat = canva_full_screen.create_rectangle(680, 80, 680 + SPACE * 4, 80 + SPACE, fill="", outline=""), \
                     canva_full_screen.create_rectangle(680, 160, SPACE * 5 + 680, 160 + SPACE, fill="", outline=""), \
                     canva_full_screen.create_rectangle(680, 240, SPACE * 3 + 680, 240 + SPACE, fill="", outline=""), \
                     canva_full_screen.create_rectangle(680, 320, SPACE * 3 + 680, 320 + SPACE, fill="", outline=""), \
                     canva_full_screen.create_rectangle(680, 400, SPACE * 2 + 680, 400 + SPACE, fill="", outline="")

    porte_avion_image = PhotoImage(file='1.png')

    porte_avion = canva_full_screen.create_image(
        (canva_full_screen.coords(canva_all_boat[1])[0] + canva_full_screen.coords(canva_all_boat[1])[2]) / 2 - 10,
        (canva_full_screen.coords(canva_all_boat[1])[1] + canva_full_screen.coords(canva_all_boat[1])[3]) / 2,
        image=porte_avion_image)

    croiseur_image = PhotoImage(file='croiseur.png')

    croiseur = canva_full_screen.create_image(
        (canva_full_screen.coords(canva_all_boat[0])[0] + canva_full_screen.coords(canva_all_boat[0])[2]) / 2,
        (canva_full_screen.coords(canva_all_boat[0])[1] + canva_full_screen.coords(canva_all_boat[0])[3]) / 2,
        image=croiseur_image)

    contretorpi1_image = PhotoImage(file='contretorpi.png')

    contretorpi1 = canva_full_screen.create_image(
        (canva_full_screen.coords(canva_all_boat[2])[0] + canva_full_screen.coords(canva_all_boat[2])[2]) / 2,
        (canva_full_screen.coords(canva_all_boat[2])[1] + canva_full_screen.coords(canva_all_boat[2])[3]) / 2,
        image=contretorpi1_image)

    contretorpi2_image = PhotoImage(file='contretorpi.png')

    contretorpi2 = canva_full_screen.create_image(
        (canva_full_screen.coords(canva_all_boat[3])[0] + canva_full_screen.coords(canva_all_boat[3])[2]) / 2,
        (canva_full_screen.coords(canva_all_boat[3])[1] + canva_full_screen.coords(canva_all_boat[3])[3]) / 2,
        image=contretorpi2_image)
    torpi1_image = PhotoImage(file='torpill.png')

    torpi1 = canva_full_screen.create_image(
        (canva_full_screen.coords(canva_all_boat[4])[0] + canva_full_screen.coords(canva_all_boat[4])[2]) / 2,
        (canva_full_screen.coords(canva_all_boat[4])[1] + canva_full_screen.coords(canva_all_boat[4])[3]) / 2,
        image=torpi1_image)

    canva_full_screen.bind("<Button-1>", partial(clic, canva_full_screen, canva_all_boat))

    canva_full_screen.bind("<Button-3>", partial(tourner, canva_full_screen, canva_all_boat))
    canva_full_screen.bind("<Button-2>", partial(tourner, canva_full_screen, canva_all_boat))

    affichage_bouton(canva_full_screen, canva_all_boat, teste_placement)


# FIN :  creation des bateaux joueurs


# Fonction permettant de deplacer, tourner , glisser,positionner correctement les bateaux du joueurs.
def clic(canva_full_screen, cnv, event):
    old[0] = event.x
    old[1] = event.y

    if (canva_full_screen.coords(cnv[0])[0] <= old[0] <= canva_full_screen.coords(cnv[0])[2]) and (
            canva_full_screen.coords(cnv[0])[1] < old[1] < canva_full_screen.coords(cnv[0])[3]):

        canva_full_screen.bind("<B1-Motion>", partial(glisser, cnv[0], canva_full_screen, croiseur))
        canva_full_screen.bind("<ButtonRelease-1>",
                               partial(lacher, canva_full_screen, cnv[0], position_bateau_1, croiseur))

    elif (canva_full_screen.coords(cnv[1])[0] <= old[0] <= canva_full_screen.coords(cnv[1])[2]) and (
            canva_full_screen.coords(cnv[1])[1] < old[1] < canva_full_screen.coords(cnv[1])[3]):
        canva_full_screen.bind("<B1-Motion>", partial(glisser, cnv[1], canva_full_screen, porte_avion))
        canva_full_screen.bind("<ButtonRelease-1>",
                               partial(lacher, canva_full_screen, cnv[1], position_bateau_2, porte_avion))

    elif (canva_full_screen.coords(cnv[2])[0] <= old[0] <= canva_full_screen.coords(cnv[2])[2]) and (
            canva_full_screen.coords(cnv[2])[1] < old[1] < canva_full_screen.coords(cnv[2])[3]):
        canva_full_screen.bind("<B1-Motion>", partial(glisser, cnv[2], canva_full_screen, contretorpi1))
        canva_full_screen.bind("<ButtonRelease-1>",
                               partial(lacher, canva_full_screen, cnv[2], position_bateau_3, contretorpi1))

    elif (canva_full_screen.coords(cnv[3])[0] <= old[0] <= canva_full_screen.coords(cnv[3])[2]) and (
            canva_full_screen.coords(cnv[3])[1] < old[1] < canva_full_screen.coords(cnv[3])[3]):
        canva_full_screen.bind("<B1-Motion>", partial(glisser, cnv[3], canva_full_screen, contretorpi2))
        canva_full_screen.bind("<ButtonRelease-1>",
                               partial(lacher, canva_full_screen, cnv[3], position_bateau_4, contretorpi2))

    elif (canva_full_screen.coords(cnv[4])[0] <= old[0] <= canva_full_screen.coords(cnv[4])[2]) and (
            canva_full_screen.coords(cnv[4])[1] < old[1] < canva_full_screen.coords(cnv[4])[3]):
        canva_full_screen.bind("<B1-Motion>", partial(glisser, cnv[4], canva_full_screen, torpi1))
        canva_full_screen.bind("<ButtonRelease-1>",
                               partial(lacher, canva_full_screen, cnv[4], position_bateau_5, torpi1))

    else:
        canva_full_screen.unbind("<B1-Motion>")


def tourner(canva_full_screen, cnv, event):
    old[0] = event.x
    old[1] = event.y

    global position_bateau_1, position_bateau_2, position_bateau_3, position_bateau_4, position_bateau_5, porte_avion_image, porte_avion, croiseur_image, croiseur, contretorpi1_image, contretorpi1, contretorpi2_image, contretorpi2, torpi1, torpi1_image
    if (canva_full_screen.coords(cnv[0])[0] <= old[0] <= canva_full_screen.coords(cnv[0])[2]) and (
            canva_full_screen.coords(cnv[0])[1] < old[1] < canva_full_screen.coords(cnv[0])[3]):
        if (position_bateau_1):

            canva_full_screen.coords(cnv[0], canva_full_screen.coords(cnv[0])[0], canva_full_screen.coords(cnv[0])[1],
                                     (canva_full_screen.coords(cnv[0])[2] - SPACE * 3),
                                     canva_full_screen.coords(cnv[0])[3] + SPACE * 3)

            position_bateau_1 = 0

            croiseur_image = PhotoImage(file='croiseur_rev.png')

            croiseur = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[0])[0] + canva_full_screen.coords(cnv[0])[2]) / 2,
                (canva_full_screen.coords(cnv[0])[1] + canva_full_screen.coords(cnv[0])[3]) / 2,
                image=croiseur_image)

        else:
            canva_full_screen.coords(cnv[0], canva_full_screen.coords(cnv[0])[0], canva_full_screen.coords(cnv[0])[1],
                                     (canva_full_screen.coords(cnv[0])[2] + SPACE * 3),
                                     canva_full_screen.coords(cnv[0])[3] - SPACE * 5)
            position_bateau_1 = 1
            croiseur_image = PhotoImage(file='croiseur.png')

            croiseur = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[0])[0] + canva_full_screen.coords(cnv[0])[2]) / 2,
                (canva_full_screen.coords(cnv[0])[1] + canva_full_screen.coords(cnv[0])[3]) / 2,
                image=croiseur_image)



    elif (canva_full_screen.coords(cnv[1])[0] <= old[0] <= canva_full_screen.coords(cnv[1])[2]) and (
            canva_full_screen.coords(cnv[1])[1] < old[1] < canva_full_screen.coords(cnv[1])[3]):
        if (position_bateau_2):

            canva_full_screen.coords(cnv[1], canva_full_screen.coords(cnv[1])[0], canva_full_screen.coords(cnv[1])[1],
                                     (canva_full_screen.coords(cnv[1])[2] - SPACE * 4),
                                     canva_full_screen.coords(cnv[1])[3] + SPACE * 4)
            position_bateau_2 = 0
            porte_avion_image = PhotoImage(file='1_rev.png')

            porte_avion = canva_full_screen.create_image((canva_full_screen.coords(cnv[1])[0] +
                                                          canva_full_screen.coords(cnv[1])[2]) / 2, (
                                                                 canva_full_screen.coords(cnv[1])[1] +
                                                                 canva_full_screen.coords(cnv[1])[3]) / 2 + 10,
                                                         image=porte_avion_image)

        else:
            canva_full_screen.coords(cnv[1], canva_full_screen.coords(cnv[1])[0], canva_full_screen.coords(cnv[1])[1],
                                     (canva_full_screen.coords(cnv[1])[2] + SPACE * 4),
                                     canva_full_screen.coords(cnv[1])[3] - SPACE * 4)
            position_bateau_2 = 1
            porte_avion_image = PhotoImage(file='1.png')

            porte_avion = canva_full_screen.create_image((canva_full_screen.coords(cnv[1])[0] +
                                                          canva_full_screen.coords(cnv[1])[2]) / 2 - 10, (
                                                                 canva_full_screen.coords(cnv[1])[1] +
                                                                 canva_full_screen.coords(cnv[1])[3]) / 2,
                                                         image=porte_avion_image)





    elif (canva_full_screen.coords(cnv[2])[0] <= old[0] <= canva_full_screen.coords(cnv[2])[2]) and (
            canva_full_screen.coords(cnv[2])[1] < old[1] < canva_full_screen.coords(cnv[2])[3]):
        if (position_bateau_3):

            canva_full_screen.coords(cnv[2], canva_full_screen.coords(cnv[2])[0], canva_full_screen.coords(cnv[2])[1],
                                     (canva_full_screen.coords(cnv[2])[2] - SPACE * 4),
                                     canva_full_screen.coords(cnv[2])[3] + SPACE * 2)
            position_bateau_3 = 0
            contretorpi1_image = PhotoImage(file='contretorpi_rev.png')

            contretorpi1 = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[2])[0] + canva_full_screen.coords(cnv[2])[2]) / 2,
                (canva_full_screen.coords(cnv[2])[1] + canva_full_screen.coords(cnv[2])[3]) / 2,
                image=contretorpi1_image)

        else:
            canva_full_screen.coords(cnv[2], canva_full_screen.coords(cnv[2])[0], canva_full_screen.coords(cnv[2])[1],
                                     (canva_full_screen.coords(cnv[2])[2] + SPACE * 2),
                                     canva_full_screen.coords(cnv[2])[3] - SPACE * 4)
            position_bateau_3 = 1
            contretorpi1_image = PhotoImage(file='contretorpi.png')

            contretorpi1 = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[2])[0] + canva_full_screen.coords(cnv[2])[2]) / 2,
                (canva_full_screen.coords(cnv[2])[1] + canva_full_screen.coords(cnv[2])[3]) / 2,
                image=contretorpi1_image)
    elif (canva_full_screen.coords(cnv[3])[0] <= old[0] <= canva_full_screen.coords(cnv[3])[2]) and (
            canva_full_screen.coords(cnv[3])[1] < old[1] < canva_full_screen.coords(cnv[3])[3]):
        if (position_bateau_4):

            canva_full_screen.coords(cnv[3], canva_full_screen.coords(cnv[3])[0], canva_full_screen.coords(cnv[3])[1],
                                     (canva_full_screen.coords(cnv[3])[2] - SPACE * 4),
                                     canva_full_screen.coords(cnv[3])[3] + SPACE * 2)
            position_bateau_4 = 0
            contretorpi2_image = PhotoImage(file='contretorpi_rev.png')

            contretorpi2 = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[3])[0] + canva_full_screen.coords(cnv[3])[2]) / 2,
                (canva_full_screen.coords(cnv[3])[1] + canva_full_screen.coords(cnv[3])[3]) / 2,
                image=contretorpi2_image)
        else:
            canva_full_screen.coords(cnv[3], canva_full_screen.coords(cnv[3])[0], canva_full_screen.coords(cnv[3])[1],
                                     (canva_full_screen.coords(cnv[3])[2] + SPACE * 2),
                                     canva_full_screen.coords(cnv[3])[3] - SPACE * 4)
            position_bateau_4 = 1
            contretorpi2_image = PhotoImage(file='contretorpi.png')

            contretorpi2 = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[3])[0] + canva_full_screen.coords(cnv[3])[2]) / 2,
                (canva_full_screen.coords(cnv[3])[1] + canva_full_screen.coords(cnv[3])[3]) / 2,
                image=contretorpi2_image)
    elif (canva_full_screen.coords(cnv[4])[0] <= old[0] <= canva_full_screen.coords(cnv[4])[2]) and (
            canva_full_screen.coords(cnv[4])[1] < old[1] < canva_full_screen.coords(cnv[4])[3]):
        if (position_bateau_5):

            canva_full_screen.coords(cnv[4], canva_full_screen.coords(cnv[4])[0], canva_full_screen.coords(cnv[4])[1],
                                     (canva_full_screen.coords(cnv[4])[2] - SPACE),
                                     canva_full_screen.coords(cnv[4])[3] + SPACE)
            position_bateau_5 = 0
            torpi1_image = PhotoImage(file='torpill_rev.png')

            torpi1 = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[4])[0] + canva_full_screen.coords(cnv[4])[2]) / 2,
                (canva_full_screen.coords(cnv[4])[1] + canva_full_screen.coords(cnv[4])[3]) / 2,
                image=torpi1_image)

        else:
            canva_full_screen.coords(cnv[4], canva_full_screen.coords(cnv[4])[0], canva_full_screen.coords(cnv[4])[1],
                                     (canva_full_screen.coords(cnv[4])[2] + SPACE),
                                     canva_full_screen.coords(cnv[4])[3] - SPACE)
            position_bateau_5 = 1
            torpi1_image = PhotoImage(file='torpill.png')

            torpi1 = canva_full_screen.create_image(
                (canva_full_screen.coords(cnv[4])[0] + canva_full_screen.coords(cnv[4])[2]) / 2,
                (canva_full_screen.coords(cnv[4])[1] + canva_full_screen.coords(cnv[4])[3]) / 2,
                image=torpi1_image)


def glisser(rect, cnv, img_bateau, event):
    cnv.move(rect, event.x - old[0], event.y - old[1])
    cnv.move(img_bateau, event.x - old[0], event.y - old[1])
    old[0] = event.x
    old[1] = event.y


def lacher(canva_full_screen, bateau, position, imgbateau, event):
    if (canva_full_screen.coords(bateau)[0] // SPACE >= 0 and canva_full_screen.coords(bateau)[
        2] // SPACE <= 10) and (
            canva_full_screen.coords(bateau)[1] // SPACE >= 0 and canva_full_screen.coords(bateau)[
        3] // SPACE <= 10):
        canva_full_screen.coords(bateau, 40 + SPACE * (canva_full_screen.coords(bateau)[0] // SPACE)
                                 , 40 + SPACE * (canva_full_screen.coords(bateau)[1] // SPACE),
                                 40 + SPACE * (canva_full_screen.coords(bateau)[2] // SPACE),
                                 40 + SPACE * (canva_full_screen.coords(bateau)[3] // SPACE))

        if position == 1:
            canva_full_screen.coords(imgbateau, (canva_full_screen.coords(bateau)[0] +
                                                 canva_full_screen.coords(bateau)[2]) / 2 - 10, (
                                             canva_full_screen.coords(bateau)[1] +
                                             canva_full_screen.coords(bateau)[3]) / 2)

        else:
            canva_full_screen.coords(imgbateau,
                                     (canva_full_screen.coords(bateau)[0] + canva_full_screen.coords(bateau)[2]) / 2, (
                                             canva_full_screen.coords(bateau)[1] + canva_full_screen.coords(bateau)[
                                         3]) / 2 + 10)


# FIN : Fonction permettant de deplacer, tourner , glisser,positionner correctement les bateaux du joueurs.


# Interaction pour commencer la partie.
def affichage_bouton(canva_full_screen, canva_all_boat, teste_placement):
    Start_the_game = Button(canva_full_screen, text='Commencer', bd=0)
    Start_the_game.configure(
        command=partial(check_boat_place, canva_full_screen, canva_all_boat, teste_placement, Start_the_game))
    Start_the_game.place(x=800, y=600)


# FIN : Interaction pour commencer la partie.


# Creation des bateaux de l'ordi et placement des bateaux aléatoirement.
def creation_bateau_ordi(canva_full_screen):
    global liste_img_ordi, place_image_bateau_ordi

    liste_img_ordi = [PhotoImage(file="contretorpi.png"), PhotoImage(file="contretorpi.png"),
                      PhotoImage(file="croiseur.png"), PhotoImage(file="torpill.png"), PhotoImage(file="1.png"),
                      PhotoImage(file="contretorpi_rev.png"), PhotoImage(file="contretorpi_rev.png"),
                      PhotoImage(file="croiseur_rev.png"), PhotoImage(file="torpill_rev.png"), PhotoImage(file="1_rev"
                                                                                                               ".png")]
    bateau2 = 0
    bateau3 = 5
    nbr_bateau3 = 10
    taille_bateaux = [5, 4, 3, 3, 2]
    global PLATEAU_ORDI
    i = 0
    while i != 5:
        valid = True

        a = randint(0, 9)
        b = randint(0, 9 - taille_bateaux[i])
        if randint(0, 1):
            for y in range(taille_bateaux[i]):
                if PLATEAU_ORDI[a][y + b] != 0:
                    valid = False
            if valid:
                # Horizontal
                if taille_bateaux[i] == 3:
                    place_image_bateau_ordi.append(
                        canva_full_screen.create_image(750 + SPACE * (y + b) - 40, 40 + SPACE * a + 30,
                                                       image=liste_img_ordi[bateau2]))
                    for y in range(taille_bateaux[i]):
                        PLATEAU_ORDI[a][y + b] = nbr_bateau3
                    nbr_bateau3 += 1
                    bateau2 += 1
                else:
                    if taille_bateaux[i] == 5:
                        place_image_bateau_ordi.append(
                            canva_full_screen.create_image(750 + SPACE * (y + b) - 80, 40 + SPACE * a + 30,
                                                           image=liste_img_ordi[4]))
                    if taille_bateaux[i] == 4:
                        place_image_bateau_ordi.append(
                            canva_full_screen.create_image(750 + SPACE * (y + b) - 60, 40 + SPACE * a + 30,
                                                           image=liste_img_ordi[2], tags="tesr"))
                    if taille_bateaux[i] == 2:
                        place_image_bateau_ordi.append(
                            canva_full_screen.create_image(750 + SPACE * (y + b) - 20, 40 + SPACE * a + 30,
                                                           image=liste_img_ordi[3]))

                    for y in range(taille_bateaux[i]):
                        PLATEAU_ORDI[a][y + b] = taille_bateaux[i]
                i = i + 1

            else:
                continue
        else:
            for y in range(taille_bateaux[i]):
                if PLATEAU_ORDI[y + b][a] != 0:
                    valid = False
            if valid:

                if taille_bateaux[i] == 3:
                    place_image_bateau_ordi.append(
                        canva_full_screen.create_image(750 + SPACE * (a) + 30, 40 + SPACE * (y + b) - 20,
                                                       image=liste_img_ordi[bateau3]))
                    for y in range(taille_bateaux[i]):
                        PLATEAU_ORDI[y + b][a] = nbr_bateau3
                    nbr_bateau3 += 1
                    bateau3 += 1
                else:
                    if taille_bateaux[i] == 5:
                        place_image_bateau_ordi.append(
                            canva_full_screen.create_image(750 + SPACE * (a) + 30, 40 + SPACE * (y + b) - 100,
                                                           image=liste_img_ordi[9], state='normal'))
                    if taille_bateaux[i] == 4:
                        place_image_bateau_ordi.append(
                            canva_full_screen.create_image(750 + SPACE * (a) + 30, 40 + SPACE * (y + b) - 75,
                                                           image=liste_img_ordi[7]))
                    if taille_bateaux[i] == 2:
                        place_image_bateau_ordi.append(
                            canva_full_screen.create_image(750 + SPACE * (a) + 30, 40 + SPACE * (y + b),
                                                           image=liste_img_ordi[8]))
                    for y in range(taille_bateaux[i]):
                        PLATEAU_ORDI[y + b][a] = taille_bateaux[i]

                i = i + 1
            else:
                continue

    for element in place_image_bateau_ordi:
        canva_full_screen.itemconfig(element, state='hidden')


# FIN : Creation des bateaux de l'ordi et placement des bateaux aléatoirement.

# Affichage des bateaux touché par le joueur + tour ordinateur
def touche(canva_full_screen):
    global posx, posy, explosion_image, all_explosion, bateauxtouchejoueur, bateauxtouchejoueur, win_affichage, image_win, image_rejouer, rejouer_tButton, image_quitter, quitter_tButton
    explosion_image.append(PhotoImage(file="explosion.png"))

    all_explosion.append(
        canva_full_screen.create_image(750 + SPACE * posy + 30, 40 + SPACE * posx + 30, image=explosion_image[0]))
    if bateauxtouchejoueur == 17:
        canva_full_screen.delete('all')
        canva_full_screen.unbind("<Button-1>")
        image_win = PhotoImage(file="win.png")
        win_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2,
                                                       image=image_win)
        image_rejouer = PhotoImage(file='rejouer.png')
        rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

        canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
        image_quitter = PhotoImage(file='quitter.png')
        quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)
        canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))
    else:
        root.after(2000, rate, canva_full_screen)


# FIN : Affichage des bateaux touché par le joueur + tour ordinateur


# Affichage des bateaux touché par l'ordinateur + tour joueur + IA

def rate(canva_full_screen):
    global rate_image, all_rate, bateauxtoucheordi, PLATEAU_JOUEUR1, image_defaite, defaite_affichage, explosion_image, all_explosion, root, image_rejouer, rejouer_tButton, image_quitter, quitter_tButton, levelia, image_win, win_affichage, stat_ordi, nbr_tir_ordi, nbr_tir_joueur, nbr_bateaux_coule_ordi, nbr_bateaux_coule_joueur, bateau_couler_par_ordi, Tour_player
    canva_full_screen.itemconfig(Tour_player, text="Tour : Joueur ",
                                 font=('Helvetica 20 bold'))
    if bateauxtouchejoueur == 17:
        canva_full_screen.delete('all')
        canva_full_screen.unbind("<Button-1>")
        image_win = PhotoImage(file="win.png")
        win_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2,
                                                       image=image_win)
    else:
        if levelia == 0:

            x = randint(0, 9)
            y = randint(0, 9)
            nbr_tir_ordi += 1
            canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                         font=('Helvetica 20 bold'))

            if PLATEAU_JOUEUR1[x][y] == 125:
                bateau_couler_par_ordi[0] += 1
                if bateau_couler_par_ordi[0] == 4:
                    nbr_bateaux_coule_ordi += 1
                    canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                        nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                 font=('Helvetica 20 bold'))

                bateauxtoucheordi = bateauxtoucheordi + 1
                if bateauxtoucheordi == 17:
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    canva_full_screen.delete('all')
                    canva_full_screen.unbind("<Button-1>")
                    image_defaite = PhotoImage(file="defaite.png")
                    defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                       root.winfo_screenheight() / 2,
                                                                       image=image_defaite)
                    image_rejouer = PhotoImage(file='rejouer.png')
                    rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                    canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                    image_quitter = PhotoImage(file='quitter.png')
                    quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                    canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                else:
                    explosion_image.append(PhotoImage(file="explosion.png"))

                    all_explosion.append(
                        canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                       image=explosion_image[0]))
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    PLATEAU_JOUEUR1[x][y] = 3
                    canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))

            elif PLATEAU_JOUEUR1[x][y] == 126:
                bateau_couler_par_ordi[1] += 1
                if bateau_couler_par_ordi[1] == 5:
                    nbr_bateaux_coule_ordi += 1
                    canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                        nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                 font=('Helvetica 20 bold'))
                bateauxtoucheordi = bateauxtoucheordi + 1
                if bateauxtoucheordi == 17:
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    canva_full_screen.delete('all')
                    canva_full_screen.unbind("<Button-1>")
                    image_defaite = PhotoImage(file="defaite.png")
                    defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                       root.winfo_screenheight() / 2,
                                                                       image=image_defaite)
                    image_rejouer = PhotoImage(file='rejouer.png')
                    rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                    canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                    image_quitter = PhotoImage(file='quitter.png')
                    quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                    canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                else:
                    explosion_image.append(PhotoImage(file="explosion.png"))

                    all_explosion.append(
                        canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                       image=explosion_image[0]))
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    PLATEAU_JOUEUR1[x][y] = 3
                    canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
            elif PLATEAU_JOUEUR1[x][y] == 127:
                bateau_couler_par_ordi[2] += 1
                if bateau_couler_par_ordi[2] == 3:
                    nbr_bateaux_coule_ordi += 1
                    canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                        nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                 font=('Helvetica 20 bold'))
                bateauxtoucheordi = bateauxtoucheordi + 1
                if bateauxtoucheordi == 17:
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    canva_full_screen.delete('all')
                    canva_full_screen.unbind("<Button-1>")
                    image_defaite = PhotoImage(file="defaite.png")
                    defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                       root.winfo_screenheight() / 2,
                                                                       image=image_defaite)
                    image_rejouer = PhotoImage(file='rejouer.png')
                    rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                    canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                    image_quitter = PhotoImage(file='quitter.png')
                    quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                    canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                else:
                    explosion_image.append(PhotoImage(file="explosion.png"))

                    all_explosion.append(
                        canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                       image=explosion_image[0]))
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    PLATEAU_JOUEUR1[x][y] = 3
                    canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
            elif PLATEAU_JOUEUR1[x][y] == 128:
                bateau_couler_par_ordi[3] += 1
                if bateau_couler_par_ordi[3] == 3:
                    nbr_bateaux_coule_ordi += 1
                    canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                        nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                 font=('Helvetica 20 bold'))

                bateauxtoucheordi = bateauxtoucheordi + 1
                if bateauxtoucheordi == 17:
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    canva_full_screen.delete('all')
                    canva_full_screen.unbind("<Button-1>")
                    image_defaite = PhotoImage(file="defaite.png")
                    defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                       root.winfo_screenheight() / 2,
                                                                       image=image_defaite)
                    image_rejouer = PhotoImage(file='rejouer.png')
                    rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                    canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                    image_quitter = PhotoImage(file='quitter.png')
                    quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                    canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                else:
                    explosion_image.append(PhotoImage(file="explosion.png"))

                    all_explosion.append(
                        canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                       image=explosion_image[0]))
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    PLATEAU_JOUEUR1[x][y] = 3
                    canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
            elif PLATEAU_JOUEUR1[x][y] == 129:
                bateau_couler_par_ordi[4] += 1
                if bateau_couler_par_ordi[4] == 2:
                    nbr_bateaux_coule_ordi += 1
                    canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                        nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                 font=('Helvetica 20 bold'))

                bateauxtoucheordi = bateauxtoucheordi + 1
                if bateauxtoucheordi == 17:
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    canva_full_screen.delete('all')
                    canva_full_screen.unbind("<Button-1>")
                    image_defaite = PhotoImage(file="defaite.png")
                    defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                       root.winfo_screenheight() / 2,
                                                                       image=image_defaite)
                    image_rejouer = PhotoImage(file='rejouer.png')
                    rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                    canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                    image_quitter = PhotoImage(file='quitter.png')
                    quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                    canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                else:
                    explosion_image.append(PhotoImage(file="explosion.png"))

                    all_explosion.append(
                        canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                       image=explosion_image[0]))
                    mixer.init()
                    soundObj = mixer.Sound('bruit_explosion.mp3')

                    soundObj.play()
                    PLATEAU_JOUEUR1[x][y] = 3
                    canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))



            elif PLATEAU_JOUEUR1[x][y] == 0:
                mixer.init()
                soundObj = mixer.Sound('bruit_eau.mp3')

                soundObj.play()
                rate_image.append(PhotoImage(file="rate.png"))

                all_rate.append(
                    canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30, image=rate_image[0]))
                canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))

                PLATEAU_JOUEUR1[x][y] = 3
            elif PLATEAU_JOUEUR1[x][y] == 3:
                rate(canva_full_screen)
        else:
            hard = [0]
            nbr_tir_ordi += 1
            canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                         font=('Helvetica 20 bold'))

            if randint(0, 1) in hard:
                x = randint(0, 9)
                y = randint(0, 9)

                if PLATEAU_JOUEUR1[x][y] == 125:
                    bateau_couler_par_ordi[0] += 1
                    if bateau_couler_par_ordi[0] == 4:
                        nbr_bateaux_coule_ordi += 1
                        canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                            nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                     font=('Helvetica 20 bold'))

                    bateauxtoucheordi = bateauxtoucheordi + 1
                    if bateauxtoucheordi == 17:
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        canva_full_screen.delete('all')
                        canva_full_screen.unbind("<Button-1>")
                        image_defaite = PhotoImage(file="defaite.png")
                        defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                           root.winfo_screenheight() / 2,
                                                                           image=image_defaite)
                        image_rejouer = PhotoImage(file='rejouer.png')
                        rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                        canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                        image_quitter = PhotoImage(file='quitter.png')
                        quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                        canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                    else:
                        explosion_image.append(PhotoImage(file="explosion.png"))

                        all_explosion.append(
                            canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                           image=explosion_image[0]))
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        PLATEAU_JOUEUR1[x][y] = 3
                        canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))

                elif PLATEAU_JOUEUR1[x][y] == 126:
                    bateau_couler_par_ordi[1] += 1
                    if bateau_couler_par_ordi[1] == 5:
                        nbr_bateaux_coule_ordi += 1
                        canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                            nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                     font=('Helvetica 20 bold'))
                    bateauxtoucheordi = bateauxtoucheordi + 1
                    if bateauxtoucheordi == 17:
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        canva_full_screen.delete('all')
                        canva_full_screen.unbind("<Button-1>")
                        image_defaite = PhotoImage(file="defaite.png")
                        defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                           root.winfo_screenheight() / 2,
                                                                           image=image_defaite)
                        image_rejouer = PhotoImage(file='rejouer.png')
                        rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                        canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                        image_quitter = PhotoImage(file='quitter.png')
                        quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                        canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                    else:
                        explosion_image.append(PhotoImage(file="explosion.png"))

                        all_explosion.append(
                            canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                           image=explosion_image[0]))
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        PLATEAU_JOUEUR1[x][y] = 3
                        canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                elif PLATEAU_JOUEUR1[x][y] == 127:
                    bateau_couler_par_ordi[2] += 1
                    if bateau_couler_par_ordi[2] == 3:
                        nbr_bateaux_coule_ordi += 1
                        canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                            nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                     font=('Helvetica 20 bold'))
                    bateauxtoucheordi = bateauxtoucheordi + 1
                    if bateauxtoucheordi == 17:
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        canva_full_screen.delete('all')
                        canva_full_screen.unbind("<Button-1>")
                        image_defaite = PhotoImage(file="defaite.png")
                        defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                           root.winfo_screenheight() / 2,
                                                                           image=image_defaite)
                        image_rejouer = PhotoImage(file='rejouer.png')
                        rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                        canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                        image_quitter = PhotoImage(file='quitter.png')
                        quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                        canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                    else:
                        explosion_image.append(PhotoImage(file="explosion.png"))

                        all_explosion.append(
                            canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                           image=explosion_image[0]))
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        PLATEAU_JOUEUR1[x][y] = 3
                        canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                elif PLATEAU_JOUEUR1[x][y] == 128:
                    bateau_couler_par_ordi[3] += 1
                    if bateau_couler_par_ordi[3] == 3:
                        nbr_bateaux_coule_ordi += 1
                        canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                            nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                     font=('Helvetica 20 bold'))

                    bateauxtoucheordi = bateauxtoucheordi + 1
                    if bateauxtoucheordi == 17:
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        canva_full_screen.delete('all')
                        canva_full_screen.unbind("<Button-1>")
                        image_defaite = PhotoImage(file="defaite.png")
                        defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                           root.winfo_screenheight() / 2,
                                                                           image=image_defaite)
                        image_rejouer = PhotoImage(file='rejouer.png')
                        rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                        canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                        image_quitter = PhotoImage(file='quitter.png')
                        quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                        canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                    else:
                        explosion_image.append(PhotoImage(file="explosion.png"))

                        all_explosion.append(
                            canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                           image=explosion_image[0]))
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        PLATEAU_JOUEUR1[x][y] = 3
                        canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                elif PLATEAU_JOUEUR1[x][y] == 129:
                    bateau_couler_par_ordi[4] += 1
                    if bateau_couler_par_ordi[4] == 2:
                        nbr_bateaux_coule_ordi += 1
                        canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                            nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                     font=('Helvetica 20 bold'))

                    bateauxtoucheordi = bateauxtoucheordi + 1
                    if bateauxtoucheordi == 17:
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        canva_full_screen.delete('all')
                        canva_full_screen.unbind("<Button-1>")
                        image_defaite = PhotoImage(file="defaite.png")
                        defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                           root.winfo_screenheight() / 2,
                                                                           image=image_defaite)
                        image_rejouer = PhotoImage(file='rejouer.png')
                        rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                        canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                        image_quitter = PhotoImage(file='quitter.png')
                        quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                        canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))


                    else:
                        explosion_image.append(PhotoImage(file="explosion.png"))

                        all_explosion.append(
                            canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                           image=explosion_image[0]))
                        mixer.init()
                        soundObj = mixer.Sound('bruit_explosion.mp3')

                        soundObj.play()
                        PLATEAU_JOUEUR1[x][y] = 3
                        canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))

                elif PLATEAU_JOUEUR1[x][y] == 0:
                    mixer.init()
                    soundObj = mixer.Sound('bruit_eau.mp3')
                    rate_image.append(PhotoImage(file="rate.png"))

                    soundObj.play()
                    all_rate.append(
                        canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30, image=rate_image[0]))
                    canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))

                    PLATEAU_JOUEUR1[x][y] = 3
                elif PLATEAU_JOUEUR1[x][y] == 3:
                    rate(canva_full_screen)
            else:

                while True:
                    x = randint(0, 9)
                    y = randint(0, 9)

                    if PLATEAU_JOUEUR1[x][y] == 125:
                        bateau_couler_par_ordi[0] += 1
                        if bateau_couler_par_ordi[0] == 4:
                            nbr_bateaux_coule_ordi += 1
                            canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                         font=('Helvetica 20 bold'))

                        bateauxtoucheordi = bateauxtoucheordi + 1
                        if bateauxtoucheordi == 17:
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            canva_full_screen.delete('all')
                            canva_full_screen.unbind("<Button-1>")
                            image_defaite = PhotoImage(file="defaite.png")
                            defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                               root.winfo_screenheight() / 2,
                                                                               image=image_defaite)
                            image_rejouer = PhotoImage(file='rejouer.png')
                            rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                            canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                            image_quitter = PhotoImage(file='quitter.png')
                            quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                            canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))
                            break


                        else:
                            explosion_image.append(PhotoImage(file="explosion.png"))

                            all_explosion.append(
                                canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                               image=explosion_image[0]))
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            PLATEAU_JOUEUR1[x][y] = 3
                            canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                            break

                    elif PLATEAU_JOUEUR1[x][y] == 126:
                        bateau_couler_par_ordi[1] += 1
                        if bateau_couler_par_ordi[1] == 5:
                            nbr_bateaux_coule_ordi += 1
                            canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                         font=('Helvetica 20 bold'))
                        bateauxtoucheordi = bateauxtoucheordi + 1
                        if bateauxtoucheordi == 17:
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            canva_full_screen.delete('all')
                            canva_full_screen.unbind("<Button-1>")
                            image_defaite = PhotoImage(file="defaite.png")
                            defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                               root.winfo_screenheight() / 2,
                                                                               image=image_defaite)
                            image_rejouer = PhotoImage(file='rejouer.png')
                            rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                            canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                            image_quitter = PhotoImage(file='quitter.png')
                            quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                            canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))
                            break

                        else:
                            explosion_image.append(PhotoImage(file="explosion.png"))

                            all_explosion.append(
                                canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                               image=explosion_image[0]))
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            PLATEAU_JOUEUR1[x][y] = 3
                            canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                            break
                    elif PLATEAU_JOUEUR1[x][y] == 127:
                        bateau_couler_par_ordi[2] += 1
                        if bateau_couler_par_ordi[2] == 3:
                            nbr_bateaux_coule_ordi += 1
                            canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                         font=('Helvetica 20 bold'))
                        bateauxtoucheordi = bateauxtoucheordi + 1
                        if bateauxtoucheordi == 17:
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            canva_full_screen.delete('all')
                            canva_full_screen.unbind("<Button-1>")
                            image_defaite = PhotoImage(file="defaite.png")
                            defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                               root.winfo_screenheight() / 2,
                                                                               image=image_defaite)
                            image_rejouer = PhotoImage(file='rejouer.png')
                            rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                            canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                            image_quitter = PhotoImage(file='quitter.png')
                            quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                            canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))

                            break
                        else:
                            explosion_image.append(PhotoImage(file="explosion.png"))

                            all_explosion.append(
                                canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                               image=explosion_image[0]))
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            PLATEAU_JOUEUR1[x][y] = 3
                            canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                            break
                    elif PLATEAU_JOUEUR1[x][y] == 128:
                        bateau_couler_par_ordi[3] += 1
                        if bateau_couler_par_ordi[3] == 3:
                            nbr_bateaux_coule_ordi += 1
                            canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                         font=('Helvetica 20 bold'))

                        bateauxtoucheordi = bateauxtoucheordi + 1
                        if bateauxtoucheordi == 17:
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            canva_full_screen.delete('all')
                            canva_full_screen.unbind("<Button-1>")
                            image_defaite = PhotoImage(file="defaite.png")
                            defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                               root.winfo_screenheight() / 2,
                                                                               image=image_defaite)
                            image_rejouer = PhotoImage(file='rejouer.png')
                            rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                            canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                            image_quitter = PhotoImage(file='quitter.png')
                            quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                            canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))

                            break
                        else:
                            explosion_image.append(PhotoImage(file="explosion.png"))

                            all_explosion.append(
                                canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                               image=explosion_image[0]))
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            PLATEAU_JOUEUR1[x][y] = 3
                            canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                            break
                    elif PLATEAU_JOUEUR1[x][y] == 129:
                        bateau_couler_par_ordi[4] += 1
                        if bateau_couler_par_ordi[4] == 2:
                            nbr_bateaux_coule_ordi += 1
                            canva_full_screen.itemconfig(stat_ordi, text="Nombre de tir : " + str(
                                nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_ordi),
                                                         font=('Helvetica 20 bold'))

                        bateauxtoucheordi = bateauxtoucheordi + 1
                        if bateauxtoucheordi == 17:
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            canva_full_screen.delete('all')
                            canva_full_screen.unbind("<Button-1>")
                            image_defaite = PhotoImage(file="defaite.png")
                            defaite_affichage = canva_full_screen.create_image(root.winfo_screenwidth() / 2,
                                                                               root.winfo_screenheight() / 2,
                                                                               image=image_defaite)
                            image_rejouer = PhotoImage(file='rejouer.png')
                            rejouer_tButton = canva_full_screen.create_image(350, 700, image=image_rejouer)

                            canva_full_screen.tag_bind(rejouer_tButton, "<Button-1>", partial(reset, root))
                            image_quitter = PhotoImage(file='quitter.png')
                            quitter_tButton = canva_full_screen.create_image(900, 700, image=image_quitter)

                            canva_full_screen.tag_bind(quitter_tButton, "<Button-1>", partial(destroy, root))
                            break

                        else:
                            explosion_image.append(PhotoImage(file="explosion.png"))

                            all_explosion.append(
                                canva_full_screen.create_image(40 + SPACE * y + 30, 40 + SPACE * x + 30,
                                                               image=explosion_image[0]))
                            mixer.init()
                            soundObj = mixer.Sound('bruit_explosion.mp3')

                            soundObj.play()
                            PLATEAU_JOUEUR1[x][y] = 3
                            canva_full_screen.bind("<Button-1>", partial(clic2_tir, canva_full_screen))
                            break
                    else:
                        continue


# FIN : Affichage des bateaux touché par l'ordinateur + tour joueur + IA

# Réaction au clic du joueur pour tirer
def clic2_tir(canva_full_screen, event):
    global PLATEAU_ORDI, posx, posy, bateauxtouchejoueur, bateauxtoucheordi, root, win_affichage, image_win, nbr_touche_bateau_4, place_image_bateau_ordi, nbr_touche_bateau_5, nbr_touche_bateau_3_1, nbr_touche_bateau_3_2, nbr_touche_bateau_2, nbr_tir_ordi, nbr_tir_joueur, nbr_bateaux_coule_ordi, nbr_bateaux_coule_joueur, stat_joueur, Tour_player

    posx = (event.y - 40) // SPACE
    posy = (event.x - 750) // SPACE

    if (0 <= int((event.x - 750) // SPACE) < 10) and (0 <= int((event.y - 40) // SPACE) < 10):
        canva_full_screen.itemconfig(Tour_player, text="Tour : Ordinateur ",
                                     font=('Helvetica 20 bold'))
        nbr_tir_joueur = nbr_tir_joueur + 1
        canva_full_screen.itemconfig(stat_joueur, text="Nombre de tir : " + str(
            nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                     font=('Helvetica 20 bold'))

        # Bateau 4 cases
        if PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] == 4:
            PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] = 3
            bateauxtouchejoueur = bateauxtouchejoueur + 1
            nbr_touche_bateau_4 += 1
            if nbr_touche_bateau_4 == 4:
                nbr_bateaux_coule_joueur += 1
                canva_full_screen.itemconfig(stat_joueur, text="Nombre de tir : " + str(
                    nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                             font=('Helvetica 20 bold'))

                canva_full_screen.itemconfig(place_image_bateau_ordi[1], state='normal')
            mixer.init()
            soundObj = mixer.Sound('bruit_explosion.mp3')

            soundObj.play()
            touche(canva_full_screen)
            canva_full_screen.unbind("<Button-1>")

        # Bateau 5 cases
        elif PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] == 5:
            PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] = 3
            bateauxtouchejoueur = bateauxtouchejoueur + 1
            nbr_touche_bateau_5 += 1
            if nbr_touche_bateau_5 == 5:
                nbr_bateaux_coule_joueur += 1
                canva_full_screen.itemconfig(stat_joueur, text="Nombre de tir : " + str(
                    nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                             font=('Helvetica 20 bold'))

                canva_full_screen.itemconfig(place_image_bateau_ordi[0], state='normal')
            mixer.init()
            soundObj = mixer.Sound('bruit_explosion.mp3')

            soundObj.play()
            touche(canva_full_screen)
            canva_full_screen.unbind("<Button-1>")
            # Bateau 3 cases : 1er

        elif PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] == 10:
            PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] = 3
            bateauxtouchejoueur = bateauxtouchejoueur + 1
            nbr_touche_bateau_3_1 += 1
            if nbr_touche_bateau_3_1 == 3:
                nbr_bateaux_coule_joueur += 1
                canva_full_screen.itemconfig(stat_joueur, text="Nombre de tir : " + str(
                    nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                             font=('Helvetica 20 bold'))

                canva_full_screen.itemconfig(place_image_bateau_ordi[2], state='normal')
            mixer.init()
            soundObj = mixer.Sound('bruit_explosion.mp3')

            soundObj.play()
            touche(canva_full_screen)
            canva_full_screen.unbind("<Button-1>")
            # Bateau 3 cases : 2eme
        elif PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] == 11:
            PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] = 3
            bateauxtouchejoueur = bateauxtouchejoueur + 1
            nbr_touche_bateau_3_2 += 1
            if nbr_touche_bateau_3_2 == 3:
                nbr_bateaux_coule_joueur += 1
                canva_full_screen.itemconfig(stat_joueur, text="Nombre de tir : " + str(
                    nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                             font=('Helvetica 20 bold'))
                canva_full_screen.itemconfig(place_image_bateau_ordi[3], state='normal')
            mixer.init()
            soundObj = mixer.Sound('bruit_explosion.mp3')

            soundObj.play()
            touche(canva_full_screen)
            canva_full_screen.unbind("<Button-1>")
        elif PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] == 2:
            PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] = 3
            bateauxtouchejoueur = bateauxtouchejoueur + 1
            nbr_touche_bateau_2 += 1
            if nbr_touche_bateau_2 == 2:
                nbr_bateaux_coule_joueur += 1
                canva_full_screen.itemconfig(stat_joueur, text="Nombre de tir : " + str(
                    nbr_tir_joueur) + "\nNombre de Bateaux coulés : " + str(nbr_bateaux_coule_joueur),
                                             font=('Helvetica 20 bold'))
                canva_full_screen.itemconfig(place_image_bateau_ordi[4], state='normal')
            mixer.init()
            soundObj = mixer.Sound('bruit_explosion.mp3')

            soundObj.play()
            touche(canva_full_screen)
            canva_full_screen.unbind("<Button-1>")


        elif PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] == 0:
            PLATEAU_ORDI[(event.y - 40) // SPACE][(event.x - 750) // SPACE] = 3
            rate_image.append(PhotoImage(file="rate.png"))
            mixer.init()
            soundObj = mixer.Sound('bruit_eau.mp3')

            soundObj.play()
            all_rate.append(
                canva_full_screen.create_image(750 + SPACE * posy + 30, 40 + SPACE * posx + 30,
                                               image=rate_image[0]))

            canva_full_screen.unbind("<Button-1>")
            root.after(2000, rate, canva_full_screen)


# FIN : Réaction au clic du joueur pour tirer
# Difficulté du bot : Facile, Difficile, affichage de la difficulté.
def level(event):
    global image_fondecran, image_canva, image_jouer, jouer_tButton, image_jouer, image_facile, facile_tButton, canva_full_screen_accueil, levelia
    if (levelia):
        image_facile = PhotoImage(file='facile.png')

        canva_full_screen_accueil.itemconfig(facile_tButton, image=image_facile)
        levelia = 0
    else:
        image_facile = PhotoImage(file='difficile.png')

        canva_full_screen_accueil.itemconfig(facile_tButton, image=image_facile)
        levelia = 1


# Lancer le jeu
def jouer(root, event):
    global image_fondecran, image_canva, image_jouer, jouer_tButton, image_jouer, image_facile, facile_tButton, canva_full_screen_accueil, levelia
    canva_full_screen_accueil.destroy()
    canva_full_screen = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="grey")

    canva_full_screen.place(x=0, y=0)
    image_fondecran = PhotoImage(file='fond_game.png')
    image_fond_game = canva_full_screen.create_image(root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2,
                                                     image=image_fondecran)

    affichage_plateau_joueur(canva_full_screen)
    creation_bateau(canva_full_screen)


# FIN : Lancer le jeu

# FIN IHM


# Controller

def main():
    global image_fondecran, image_canva, image_jouer, jouer_tButton, image_jouer, image_facile, facile_tButton, canva_full_screen_accueil, root

    root = Tk()

    # root.attributes('-fullscreen', True)
    root.title("Bataille Navale")
    root.geometry("1440x900")
    canva_full_screen_accueil = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(),
                                       bg="grey")
    canva_full_screen_accueil.place(x=0, y=0)
    image_fondecran = PhotoImage(file='fond.png')
    image_facile = PhotoImage(file='Facile.png')

    image_jouer = PhotoImage(file='jouer.png')

    image_canva = canva_full_screen_accueil.create_image(root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2,
                                                         image=image_fondecran)

    jouer_tButton = canva_full_screen_accueil.create_image(450, 350, image=image_jouer)
    facile_tButton = canva_full_screen_accueil.create_image(450, 650, image=image_facile)

    canva_full_screen_accueil.tag_bind(jouer_tButton, "<Button-1>", partial(jouer, root))
    facile_tButton = canva_full_screen_accueil.create_image(450, 650, image=image_facile)
    canva_full_screen_accueil.tag_bind(facile_tButton, "<Button-1>", level)

    root.mainloop()


main()
# FIN : Controller
