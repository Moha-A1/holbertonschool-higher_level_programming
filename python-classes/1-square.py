#!/usr/bin/python3
"""
Module qui définit une classe Square avec un attribut privé size.
Ce module contient une classe Square avec un attribut privé pour la taille.
"""


class Square:
    """
    Une classe qui définit un carré avec un attribut privé size.

    Cette classe crée un objet carré avec une taille privée
    qui ne peut pas être accédée directement depuis l'extérieur.
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size: La taille du côté du carré.
        """
        self.__size = size
