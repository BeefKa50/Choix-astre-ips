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
    student.used_softwares["LabView"] = row[columns["labview"]]
    student.used_softwares["Excel"] = row[columns["excel"]]
    student.used_softwares["Blender"] = row[columns["blender"]]
    student.used_softwares["Unity"] = row[columns["unity"]]
    student.used_softwares["Figma"] = row[columns["figma"]]
    student.used_softwares["Cisco Packet Tracer"] = row[columns["cisco"]]
    student.used_softwares["SolidWorks"] = row[columns["solidworks"]]
    student.used_softwares["AutoCAD"] = row[columns["autocad"]]
    student.ensim_machines = str(row[columns["machines_ensim"]]).split(",")

    for machine in student.ensim_machines:
        if machine == " Rien":
            student.ensim_machines.remove(" Rien")
            student.ensim_machines.remove(" les ordis c’est très bien")
            student.ensim_machines.append("Rien, les ordis c'est très bien")
            break

    student.associations["Kartel"] = row[columns["kartel"]]
    student.associations["Ensimersion"] = row[columns["ensimersion"]]
    student.associations["Ensim'Elec"] = row[columns["ensimelec"]]
    student.associations["Enigma"] = row[columns["enigma"]]
    student.associations["L'Ensimien"] = row[columns["lensimien"]]
    student.object_to_3d_print = row[columns["imprimante_3d"]]
    student.hobbies = str(row[columns["hobbies"]]).split(",")
    student.is_using_color_palette = True if str(row[columns["palettes_couleurs"]]) == "Oui" else False
    student.action_when_crash = row[columns["panne_ordinateur"]]
    student.studies_before_ensim = row[columns["etudes_avant_ensim"]]
    student.fav_os = row[columns["os_pref"]]