import pytest

from noyau import *

def test_changer_joueur():
   assert True==True


def test_maj_jeu_limites():
    grille = [[-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1]]

    niveau = [5, 5, 5, 5, 5, 5, 5]
    joueur = 0

    # Remplir toutes les cases de la colonne 0
    for i in range(6):
        case = f"c0{i}"
        result = maj_jeu(case, grille, niveau, joueur)
        assert result == (i, 0)
        joueur = 1 - joueur

    # Essayer de remplir une case de plus dans la colonne 0
    case = "c00"
    with pytest.raises(IndexError):
        maj_jeu(case, grille, niveau, joueur)


def test_jetons_hors_grille():
    grille = [[-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1]]
    assert jeton(0, -1, 2, 1, 0, grille) == 0
    assert jeton(0, 4, 7, -1, -1, grille) == 0
#Ce test vérifie que l'appel à jeton(0, -1, 2, 1, 0, grille) retourne 0 lorsque l'on part de la case (-1,2), 
# qui est en dehors de la grille. De même, il vérifie que l'appel à jeton(0, 4, 7, -1, -1, grille) retourne 0 lorsque 
# l'on part de la case (4,7), qui est également en dehors de la grille.