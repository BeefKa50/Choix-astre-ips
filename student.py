import numpy as np
from django.db import models

from functions import hypothesis


class Student:
    def __init__(self):
        self.id = "e000000"
        self.engineer_definition = ""
        self.procedural_ease = ""
        self.object_oriented_ease = ""
        self.functional_ease = ""
        self.technology_interest = {}
        self.high_school_subjects = []
        self.s5_fav_subjects = []
        self.used_softwares = {}
        self.ensim_machines = []
        self.associations = {}
        self.object_to_3d_print = ""
        self.hobbies = []
        self.is_using_color_palette = False
        self.action_when_crash = ""
        self.studies_before_ensim = ""
        self.fav_os = ""

    def answersAsArray(self):
        answers_array = {}
        for key,value in hypothesis.items():
            answers_array[key] = 0

        if self.engineer_definition == "C’est avant tout un cadre supérieur technique qui " \
                                       "a pour mission de piloter un projet et de gérer une " \
                                       "ou plusieurs équipes en interface avec le client.":

            answers_array["Ingénieur chef de projet"] = hypothesis["Ingénieur chef de projet"]

        elif self.engineer_definition == "Un ingénieur est un Homme capable de prendre du recul et " \
                                         "d’avoir une solide culture générale, technique et humaine.":

            answers_array["Ingénieur, homme de culture"] = hypothesis["Ingénieur, homme de culture"]

        else:
            answers_array["Ingénieur expert technique"] = hypothesis["Ingénieur expert technique"]

        answers_array["Procédural"] = hypothesis["Procédural"]*((self.procedural_ease-1)/2)
        answers_array["Orienté objet"] = hypothesis["Orienté objet"] * ((self.object_oriented_ease - 1) / 2)
        answers_array["Fonctionnel"] = hypothesis["Fonctionnel"] * ((self.functional_ease - 1) / 2)

        answers_array["Web"] = hypothesis["Web"] * ((self.technology_interest["Web"]) / 5)
        answers_array["Cloud"] = hypothesis["Cloud"] * ((self.technology_interest["Cloud"]) / 5)
        answers_array["Embarqué"] = hypothesis["Embarqué"] * ((self.technology_interest["Embedded"]) / 5)
        answers_array["Mobile"] = hypothesis["Mobile"] * ((self.technology_interest["Mobile"]) / 5)
        answers_array["Développement de jeux vidéos"] = hypothesis["Développement de jeux vidéos"] * \
                                                        ((self.technology_interest["Videogames"]) / 5)

        for subject in self.high_school_subjects:
            if subject == "Maths" or subject == " Maths":
                answers_array["Mathématiques"] = hypothesis["Mathématiques"]
            elif subject == "Physique/Chimie" or subject == " Physique/Chimie":
                answers_array["Physique-Chimie"] = hypothesis["Physique-Chimie"]
            elif subject == "Littérature/Philosophie" or subject == " Littérature/Philosophie":
                answers_array["Littérature et Philosophie"] = hypothesis["Littérature et Philosophie"]
            elif subject == "Histoire/Géographie" or subject == " Histoire/Géographie":
                answers_array["Histoire Géographie"] = hypothesis["Histoire Géographie"]
            elif subject == "Sciences de gestion" or subject == " Sciences de gestion":
                answers_array["Gestion"] = hypothesis["Gestion"]
            elif subject == "Arts Plastiques/Arts appliqués" or subject == " Arts Plastiques/Arts appliqués":
                answers_array["Arts appliqués"] = hypothesis["Arts appliqués"]
            elif subject == "Sciences de l'ingénieur" or subject == " Sciences de l'ingénieur":
                answers_array["Sciences de l'ingenieur"] = hypothesis["Sciences de l'ingenieur"]

        for sub_s5 in self.s5_fav_subjects:
            if sub_s5 == "Cryptographie (en Maths)" or sub_s5 == " Cryptographie (en Maths)":
                answers_array["S5 cryptographie"] = hypothesis["S5 cryptographie"]
            elif sub_s5 == "Physique" or sub_s5 == " Physique":
                answers_array["S5 physique"] = hypothesis["S5 physique"]
            elif sub_s5 == "Anglais" or sub_s5 == " Anglais":
                answers_array["S5 anglais"] = answers_array["S5 anglais"]
            elif sub_s5 == "Conduite de projet" or sub_s5 == " Conduite de projet":
                answers_array["S5 conduite de projet"] = hypothesis["S5 conduite de projet"]
            elif sub_s5 == "Droit du travail" or sub_s5 == " Droit du travail":
                answers_array["S5 droit du travail"] = hypothesis["S5 droit du travail"]
            elif sub_s5 == "Electronique" or sub_s5 == " Electronique":
                answers_array["S5 Électronique"] = hypothesis["S5 Électronique"]
            elif sub_s5 == "Programmation informatique" or sub_s5 == " Programmation informatique":
                answers_array["S5 Programmation"] = hypothesis["S5 Programmation"]
            elif sub_s5 == "Algorithmique" or sub_s5 == " Algorithmique":
                answers_array["S5 Algorithmique"] = hypothesis["S5 Algorithmique"]
            elif sub_s5 == "Technologie de l’internet" or sub_s5 == " Technologie de l’internet":
                answers_array["S5 Technologie de l'internet"] = hypothesis["S5 Technologie de l'internet"]
            elif sub_s5 == "Architecture des ordinateurs" or sub_s5 == " Architecture des ordinateurs":
                answers_array["S5 Architecture des ordinateurs"] = hypothesis["S5 Architecture des ordinateurs"]
            elif sub_s5 == "Logique combinatoire et séquentielle" or sub_s5 == " Logique combinatoire et séquentielle":
                answers_array["S5 Logique combinatoire et séquentielle"] = \
                    hypothesis["S5 Logique combinatoire et séquentielle"]
            elif sub_s5 == "Introduction aux IHM" or sub_s5 == " Introduction aux IHM":
                answers_array["S5 Introduction aux IHM"] = hypothesis["S5 Introduction aux IHM"]

        answers_array["LabView"] = hypothesis["LabView"] * ((self.used_softwares["LabView"]-1) / 4)
        answers_array["Excel"] = hypothesis["Excel"] * ((self.used_softwares["Excel"] - 1) / 4)
        answers_array["Blender"] = hypothesis["Blender"] * ((self.used_softwares["Blender"] - 1) / 4)
        answers_array["Unity"] = hypothesis["Unity"] * ((self.used_softwares["Unity"] - 1) / 4)
        answers_array["Figma"] = hypothesis["Figma"] * ((self.used_softwares["Figma"] - 1) / 4)
        answers_array["Cisco Packet Tracer"] = hypothesis["Cisco Packet Tracer"] * \
                                               ((self.used_softwares["Cisco Packet Tracer"] - 1) / 4)
        answers_array["SolidWorks"] = hypothesis["SolidWorks"] * ((self.used_softwares["SolidWorks"] - 1) / 4)
        answers_array["AutoCAD"] = hypothesis["AutoCAD"] * ((self.used_softwares["AutoCAD"] - 1) / 4)

        for machine in self.ensim_machines:
            if machine == "Imprimante 3D" or machine == " Imprimante 3D":
                answers_array["Imprimante 3D"] = hypothesis["Imprimante 3D"]
            elif machine == "Drone" or machine == " Drone":
                answers_array["Drone"] = hypothesis["Drone"]
            elif machine == "Casque VR" or machine == " Casque VR":
                answers_array["Casque VR"] = hypothesis["Casque VR"]
            elif machine == "Cartes électroniques programmables (Arduino, Raspberry...)" or machine == \
                    " Cartes électroniques programmables (Arduino, Raspberry...)":
                answers_array["Carte électronique programmable"] = hypothesis["Carte électronique programmable"]
            elif machine == "Oscilloscope" or machine == " Oscilloscope":
                answers_array["Oscilloscope"] = hypothesis["Oscilloscope"]
            elif machine == "Casque neuronal" or machine == " Casque neuronal":
                answers_array["Casque neuronal"] = hypothesis["Casque neuronal"]
            elif machine == "Smartphones" or machine == " Smartphones":
                answers_array["Smartphone"] = hypothesis["Smartphone"]
            elif machine == "Rien, les ordis c’est très bien" or machine == " Rien, les ordis c’est très bien":
                answers_array["Rien"] = hypothesis["Rien"]

        answers_array["K[art]el"] = hypothesis["K[art]el"] * ((self.associations["Kartel"] - 1) / 3)
        answers_array["Ensimersion"] = hypothesis["Ensimersion"] * ((self.associations["Ensimersion"] - 1) / 3)
        answers_array["Ensim'Elec"] = hypothesis["Ensim'Elec"] * ((self.associations["Ensim'Elec"] - 1) / 3)
        answers_array["Enigma"] = hypothesis["Enigma"] * ((self.associations["Enigma"] - 1) / 3)
        answers_array["Enigma"] = hypothesis["Enigma"] * ((self.associations["Enigma"] - 1) / 3)
        answers_array["L'Ensimien"] = hypothesis["L'Ensimien"] * ((self.associations["L'Ensimien"] - 1) / 3)

        if self.object_to_3d_print == "Statue de Mario":
            answers_array["Statue de Mario"] = hypothesis["Statue de Mario"]

        elif self.object_to_3d_print == "Des boutons":
            answers_array["Bouton"] = hypothesis["Bouton"]

        elif self.object_to_3d_print == "Boitier pour sa carte arduino":
            answers_array["Boîtier pour carte Arduino"] = hypothesis["Boîtier pour carte Arduino"]

        for hobby in self.hobbies:
            if hobby == "Lecture" or hobby == " Lecture":
                answers_array["Lecture"] = hypothesis["Lecture"]
            elif hobby == "Bricolage" or hobby == " Bricolage":
                answers_array["Bricolage"] = hypothesis["Bricolage"]
            elif hobby == "Sport" or hobby == " Sport":
                answers_array["Sport"] = hypothesis["Sport"]
            elif hobby == "Art Dessin" or hobby == " Art Dessin":
                answers_array["Art et dessin"] = hypothesis["Art et dessin"]
            elif hobby == "Jeux vidéos" or hobby == " Jeux vidéos":
                answers_array["Jeux vidéos"] = hypothesis["Jeux vidéos"]
            elif hobby == "Musique" or hobby == " Musique":
                answers_array["Musique"] = hypothesis["Musique"]
            elif hobby == "Musculation" or hobby == " Musculation":
                answers_array["Musculation"] = hypothesis["Musculation"]

        answers_array["Utilisation de palettes de couleur"] = hypothesis[
            "Utilisation de palettes de couleur"] if self.is_using_color_palette else 0

        answers_array["Non utilisation de palettes de couleurs"] = hypothesis[
            "Non utilisation de palettes de couleurs"] if not self.is_using_color_palette else 0

        if self.action_when_crash == "Vous le démontez pour comprendre d'où vient le problème":
            answers_array["Démontage du PC"] = hypothesis["Démontage du PC"]

        elif self.action_when_crash == "Vous essayez de le réparer en passant par le BIOS":
            answers_array["Réparation par le BIOS"] = hypothesis["Réparation par le BIOS"]

        elif self.action_when_crash == "Vous allez voir un réparateur":
            answers_array["Consulter un réparateur"] = hypothesis["Consulter un réparateur"]

        else:
            answers_array["Acheter un nouveau PC"] = hypothesis["Acheter un nouveau PC"]


        if self.studies_before_ensim == "BTS SIO":
            answers_array["BTS SIO"] = hypothesis["BTS SIO"]

        elif self.studies_before_ensim == "BTS SN":
            answers_array["BTS SN"] = hypothesis["BTS SN"]

        elif self.studies_before_ensim == "Prépa intégré":
            answers_array["Prépa intégrée"] = hypothesis["Prépa intégrée"]

        elif self.studies_before_ensim == "CPGE MP2I/MPSI":
            answers_array["CPGE MPSI"] = hypothesis["CPGE MPSI"]


        elif self.studies_before_ensim == "CPGE MP":
            answers_array["CPGE MP"] = hypothesis["CPGE MP"]

        elif self.studies_before_ensim == "CPGE BL":
            answers_array["CPGE BL"] = hypothesis["CPGE BL"]

        elif self.studies_before_ensim == "CPGE ATS":
            answers_array["CPGE ATS"] = hypothesis["CPGE ATS"]

        elif self.studies_before_ensim == "CPGE PC":
            answers_array["CPGE PC"] = hypothesis["CPGE PC"]

        elif self.studies_before_ensim == "CPGE TSi":
            answers_array["CPGE TSI"] = hypothesis["CPGE TSI"]

        elif self.studies_before_ensim == "CPGE PT":
            answers_array["CPGE PT"] = hypothesis["CPGE PT"]

        elif self.studies_before_ensim == "DUT Informatique":
            answers_array["DUT Informatique"] = hypothesis["DUT Informatique"]

        elif self.studies_before_ensim == "DUT Métiers du Multimédia et Interne":
            answers_array["DUT Métiers du multimédia et de l'internet"] = hypothesis[
                "DUT Métiers du multimédia et de l'internet"]

        elif self.studies_before_ensim == "L2, L3 informatique":
            answers_array["L2/L3 Informatique"] = hypothesis["L2/L3 Informatique"]

        else:
            answers_array["M1/M2 Informatique"] = hypothesis["M1/M2 Informatique"]

        if self.fav_os == "Windows":
            answers_array["Windows"] = hypothesis["Windows"]

        elif self.fav_os == "MacOS":
            answers_array["MacOS"] = hypothesis["MacOS"]

        else:
            answers_array["Linux"] = hypothesis["Linux"]

        return answers_array