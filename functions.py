# Column names in the csv file
columns = {"date":"Horodateur",
           "num":"1. Quel est votre numéro étudiant ? (ex: e22XXXX)",
           "def_inge":"2. Quelle est la définition d’un ingénieur qui vous correspond le mieux ?",
           "procedural":"3. Êtes-vous plutôt programmation ... [Procédurale]",
           "objet":"3. Êtes-vous plutôt programmation ... [Orienté Object]",
           "fonctionnelle":"3. Êtes-vous plutôt programmation ... [Fonctionnelle]",
           "interet_web":"4. Quel est votre degré d'intérêt pour ces technologies ? (0 → aucun intérêt, 5 → passionné)   [Web (HTML, CSS , PHP , CMS)]",
           "interet_cloud":"4. Quel est votre degré d'intérêt pour ces technologies ? (0 → aucun intérêt, 5 → passionné)   [Cloud (Azure, AWS,GCP)]",
           "interet_embarque":"4. Quel est votre degré d'intérêt pour ces technologies ? (0 → aucun intérêt, 5 → passionné)   [Embarqué (Arduino, Assembleur, Raspberry...)]",
           "interet_mobile":"4. Quel est votre degré d'intérêt pour ces technologies ? (0 → aucun intérêt, 5 → passionné)   [Mobile (Android, iOS,Cross-platform) ]",
           "interet_jeux_videos":"4. Quel est votre degré d'intérêt pour ces technologies ? (0 → aucun intérêt, 5 → passionné)   [Dev Jeux vidéo (Unity, Unreal Engine)]",
           "matiere_lycee":"5. Quelle(s) matière(s) avez-vous aimé particulièrement au lycée parmi les suivantes : ",
           "cours_S5":"6. Quel(s) cours avez-vous aimé particulièrement au semestre S5 ?",
           "labview":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [LabView]",
           "excel":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [Excel]",
           "blender":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [Blender]",
           "unity":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [Unity]",
           "figma":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [Figma]",
           "cisco":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [Cisco Packet Tracer]",
           "solidworks":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [SolidWorks]",
           "autocad":"7. Quels logiciels / applications avez-vous l’habitude (ou avez-vous déjà utilisé) d’utiliser ?  [AutoCAD]",
           "machines_ensim":"8. Parmi ces machines, lesquelles espérez-vous pouvoir utiliser au cours de vos projets d’année ? ",
           "kartel":"9. De quelles associations faites-vous partie ? Ou souhaitez-vous rejoindre? [K[art]el]",
           "ensimersion":"9. De quelles associations faites-vous partie ? Ou souhaitez-vous rejoindre? [Ensimersion]",
           "ensimelec":"9. De quelles associations faites-vous partie ? Ou souhaitez-vous rejoindre? [Ensim’elec]",
           "enigma":"9. De quelles associations faites-vous partie ? Ou souhaitez-vous rejoindre? [Enigma]",
           "lensimien":"9. De quelles associations faites-vous partie ? Ou souhaitez-vous rejoindre? [L'Ensimien]",
           "imprimante_3d":"10. Si on vous donne une imprimante 3D, qu'est-ce que vous imprimez d’abord ?",
           "hobbies":"11. Quels sont vos hobbies ?",
           "palettes_couleurs":"12. Utilisez-vous des sites pour créer une palette de couleurs ?",
           "panne_ordinateur":"13. Votre ordinateur tombe en panne, que faites vous ?",
           "etudes_avant_ensim":"14. Qu’avez-vous fait avant le cycle ingénieur ?",
           "os_pref":"15. Quel est ton système d’exploitation que tu utilises le plus pour développer ?"}

# Initial coefficients for each answer (1)
hypothesis = {"Ingénieur expert technique":1,"Ingénieur, homme de culture":1,"Ingénieur chef de projet":1,
              "Procédural":1,"Orienté objet":1,"Fonctionnel":1,"Web":1,"Cloud":1,"Embarqué":1,"Mobile":1,
              "Développement de jeux vidéos":1,"Mathématiques":1,"Physique-Chimie":1,
              "Littérature et Philosophie":1,"Histoire Géographie":1,"Gestion":1,"Arts appliqués":1,"Sciences de l'ingenieur":1,
              "S5 cryptographie":1,"S5 physique":1,"S5 anglais":1,"S5 conduite de projet":1,"S5 droit du travail":1,
              "S5 Électronique":1,"S5 Programmation":1,"S5 Algorithmique":1,"S5 Technologie de l'internet":1,
              "S5 Architecture des ordinateurs":1,"S5 Logique combinatoire et séquentielle":1,
              "S5 Introduction aux IHM":1,"LabView":1, "Excel":1, "Blender":1, "Unity":1, "Figma":1,
              "Cisco Packet Tracer":1, "SolidWorks":1, "AutoCAD":1,"Imprimante 3D":1, "Drone":1, "Casque VR":1,
              "Carte électronique programmable":1, "Oscilloscope":1, "Casque neuronal":1, "Smartphone":1, "Rien":1,
              "K[art]el":1, "Ensimersion":1, "Ensim'Elec":1, "Enigma":1, "L'Ensimien":1, "Statue de Mario":1,
              "Boîtier pour carte Arduino":1, "Bouton":1, "Coque de téléphone":1, "Lecture":1, "Bricolage":1,
              "Sport":1, "Art et dessin":1, "Jeux vidéos":1, "Musique":1, "Musculation":1,
              "Utilisation de palettes de couleur":1, "Non utilisation de palettes de couleurs":1, "Démontage du PC":1
              , "Réparation par le BIOS":1, "Consulter un réparateur":1, "Acheter un nouveau PC":1, "Prépa intégrée":1,
              "CPGE ATS":1, "CPGE PT":1, "CPGE TSI":1, "CPGE MP":1, "CPGE MPSI":1, "CPGE BL":1, "CPGE PC":1,
              "BTS SIO":1, "BTS SN":1, "DUT Informatique":1, "DUT Métiers du multimédia et de l'internet":1,
              "L2/L3 Informatique":1, "M1/M2 Informatique":1, "Windows":1, "MacOS":1, "Linux":1}

# Transform a string value to a numeric value in a range
def assign_value_to_string_answer(answer):
    if answer == "Ne connais pas":
        return 1
    elif answer == "Jamais":
        return 2
    elif answer == "Un peu":
        return 3
    elif answer == "Régulièrement":
        return 4
    elif answer == "Tout le temps":
        return 5

# Transform a string value to a numeric value in a range
def assign_value_to_string_answer_asso(answer):
    if answer == "J'y suis":
        return 4
    elif answer == "Interest":
        return 3
    elif answer == "Ne connais pas":
        return 1
    elif answer == "Pas intéressé":
        return 2

# Initialize a Student object with its line in the csv file
def initializeStudent(student,row):

    student.id = row[columns["num"]]
    student.engineer_definition = row[columns["def_inge"]]
    student.procedural_ease = row[columns["procedural"]]
    student.object_oriented_ease = row[columns["objet"]]
    student.functional_ease = row[columns["fonctionnelle"]]
    student.technology_interest["Web"] = row[columns["interet_web"]]
    student.technology_interest["Cloud"] = row[columns["interet_cloud"]]
    student.technology_interest["Embedded"] = row[columns["interet_embarque"]]
    student.technology_interest["Mobile"] = row[columns["interet_mobile"]]
    student.technology_interest["Videogames"] = row[columns["interet_jeux_videos"]]
    student.high_school_subjects = str(row[columns["matiere_lycee"]]).split(",")
    student.s5_fav_subjects = str(row[columns["cours_S5"]]).split(",")
    student.used_softwares["LabView"] = assign_value_to_string_answer(row[columns["labview"]])
    student.used_softwares["Excel"] = assign_value_to_string_answer(row[columns["excel"]])
    student.used_softwares["Blender"] = assign_value_to_string_answer(row[columns["blender"]])
    student.used_softwares["Unity"] = assign_value_to_string_answer(row[columns["unity"]])
    student.used_softwares["Figma"] = assign_value_to_string_answer(row[columns["figma"]])
    student.used_softwares["Cisco Packet Tracer"] = assign_value_to_string_answer(row[columns["cisco"]])
    student.used_softwares["SolidWorks"] = assign_value_to_string_answer(row[columns["solidworks"]])
    student.used_softwares["AutoCAD"] = assign_value_to_string_answer(row[columns["autocad"]])
    student.ensim_machines = str(row[columns["machines_ensim"]]).split(",")

    for machine in student.ensim_machines:
        if machine == " Rien":
            student.ensim_machines.remove(" Rien")
            student.ensim_machines.remove(" les ordis c’est très bien")
            student.ensim_machines.append("Rien, les ordis c'est très bien")
            break
        if machine == "Rien":
            student.ensim_machines.remove("Rien")
            student.ensim_machines.remove(" les ordis c’est très bien")
            student.ensim_machines.append("Rien, les ordis c'est très bien")

        if machine == " Cartes électroniques programmables (Arduino":
            student.ensim_machines.remove(" Cartes électroniques programmables (Arduino")
            student.ensim_machines.remove(" Raspberry...)")
            student.ensim_machines.append("Cartes électroniques programmables (Arduino, Raspberry...)")
            break
        if machine == "Cartes électroniques programmables (Arduino":
            student.ensim_machines.remove("Cartes électroniques programmables (Arduino")
            student.ensim_machines.remove(" Raspberry...)")
            student.ensim_machines.append("Cartes électroniques programmables (Arduino, Raspberry...)")

    student.associations["Kartel"] = assign_value_to_string_answer_asso(row[columns["kartel"]])
    student.associations["Ensimersion"] = assign_value_to_string_answer_asso(row[columns["ensimersion"]])
    student.associations["Ensim'Elec"] = assign_value_to_string_answer_asso(row[columns["ensimelec"]])
    student.associations["Enigma"] = assign_value_to_string_answer_asso(row[columns["enigma"]])
    student.associations["L'Ensimien"] = assign_value_to_string_answer_asso(row[columns["lensimien"]])
    student.object_to_3d_print = row[columns["imprimante_3d"]]
    student.hobbies = str(row[columns["hobbies"]]).split(",")
    student.is_using_color_palette = True if str(row[columns["palettes_couleurs"]]) == "Oui" else False
    student.action_when_crash = row[columns["panne_ordinateur"]]
    student.studies_before_ensim = row[columns["etudes_avant_ensim"]]
    student.fav_os = row[columns["os_pref"]]
