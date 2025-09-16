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

    @property
    def size(self):
        """
        Getter pour l'attribut size

        Returns:
            int: La taille du côté du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut size

        Args:
            value (int): La nouvelle taille du côté du carré

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        # Vérification que value est un entier
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Vérification que value n'est pas négatif
        if value < 0:
            raise ValueError("size must be >= 0")

        # Mise à jour de la taille
        self.__size = value

    def area(self):
        """
        Calcule et retourne l'aire du carré

        Returns:
            int: L'aire du carré (size * size)
        """
        return self.__size * self.__size
