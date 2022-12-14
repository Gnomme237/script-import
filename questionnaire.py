# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

import json

class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromJsonData(data):
#On fait une complétion de liste sur la variable choix en récupérant uniquement les titres des différents choix.
        choix = [i[0] for i in data["choix"]]
        bonne_reponse = [i[0] for i in data["choix"]if i[1] == True]
        if len(bonne_reponse) != 1:
            return None
        q = Question(data["titre"], choix, bonne_reponse[0])
        return q
#Nb: i[0] est l'indice du titre de la question et i[1] est l'indice du 1er element de "choix"
#Nb: La bonne réponse est trouvé en faisant avec un choix pour le "True".
    def poser(self, num_question, nb_questions):
        print(f"QUESTION {num_question} / {nb_questions}")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions, categorie, titre, difficulte):
        self.questions = questions
        self.categorie = categorie
        self.titre = titre
        self.difficulte = difficulte
    def FromJsonData(data):
        questionnaire_data_questions = data["questions"]
        questions = [Question.FromJsonData(i) for i in questionnaire_data_questions]

        return Questionnaire(questions, data["categorie"], data["titre"], data["difficulte"])
    def lancer(self):
        score = 0
        nb_questions = len(self.questions)

        print("-------")
        print("QUESTIONNAIRES: " + self.titre)
        print("Categorie: " + self.titre)
        print("Difficulté:" + self.difficulte)
        print("Nombre de questions: " + str(nb_questions))
        print("-------")

        for i in range(nb_questions):
            question = self.questions[i]
            if question.poser(i+1, nb_questions):
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

"""Questionnaire(
    (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()
"""
#Charger le fichier JSON

filename = "cinema_starwars_debutant.json"
file = open(filename, "r")
json_data = file.read()
file.close()
questionnaire_data = json.loads(json_data)


#q = Question.FromJsonData(questionnaire_data_questions[0])  #"Question" est celui de la class

#Questionnaire(questions).lancer()

Questionnaire.FromJsonData(questionnaire_data).lancer()

#q.poser()

#"questions" est le paramètre de Questionnaire. Mettez un point d'arret et lancer le débogueur pour mieux comprendre.
print("end")


