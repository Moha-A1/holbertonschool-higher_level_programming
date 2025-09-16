#!/usr/bin/python3
"""
Module contenant la classe Square
Cette classe représente un carré avec une taille donnée
"""


class Square:
    """
    Classe qui définit un carré

    Attributs:
        __size (int): La taille du côté du carré (attribut privé)
    """

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square

        Args:
            size (int): La taille du côté du carré. Par défaut 0.

        Raises:
            TypeError: Si size n'est pas un entier
            ValueError: Si size est négatif
        """
        # Vérification que size est un entier
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Vérification que size n'est pas négatif
        if size < 0:
            raise ValueError("size must be >= 0")

        # Stockage de la taille dans un attribut privé
        self.__size = size
