#!/usr/bin/python3
"""
Module pour afficher un nom complet
Contient une fonction pour afficher
le prénom et nom d'une personne
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche le nom complet d'une personne
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
