from Lib.classes.roi_sorcier import RoiSorcier
from Lib.classes.magicien import Magicien
from Lib.custom import printlbl as p
import random as r

class BattleManager():
    
    def launch(self):
        rs_pv = 100
        m_pv = 100
        rs_degats = 10 + r.randint(-2, 2)
        m_degats = 10 + r.randint(-2, 2)
        base_experience = 0
        exp_rate_1 = 1 + (r.randint(0, 1) / 10)
        exp_rate_2 = 1 + (r.randint(0, 1) / 10)
        # On donne l'exp rate le plus élevé à celui qui fait le moins de dégâts
        if rs_degats < m_degats:
            rs_exp_rate = max(exp_rate_1, exp_rate_2)
            m_exp_rate = min(exp_rate_1, exp_rate_2)
        else:
            rs_exp_rate = min(exp_rate_1, exp_rate_2)
            m_exp_rate = max(exp_rate_1, exp_rate_2)
        turnOrder = r.randint(1, 2)
        if turnOrder == 1:
            rs_turn = 'joueur1'
            m_turn = 'joueur2'
        else:
            rs_turn = 'joueur2'
            m_turn = 'joueur1'
        roi_sorcier = RoiSorcier("Roi Sorcier", rs_pv, rs_degats, base_experience, rs_exp_rate, rs_turn)
        magicien = Magicien("Magicien", m_pv, m_degats, base_experience, m_exp_rate, m_turn)  
        BattleManager.battle(roi_sorcier, magicien)
        
        
        
    @staticmethod
    def battle(roi_sorcier: RoiSorcier, magicien: Magicien):
        turnNumber = 1
        p.print_lbl("Début du combat ! 🤺")
        p.print_lbl(f"Tour {turnNumber} :\n{roi_sorcier.nom} a {roi_sorcier.vie} PV et {magicien.nom} a {magicien.vie} PV.")
        p.print_lbl(f"EXP Actuelles : {roi_sorcier.experience} EXP pour {roi_sorcier.nom} et {magicien.experience} EXP pour {magicien.nom}.")
        p.print_lbl(f"GO !! ⚔\n-----------------")
        while roi_sorcier.vie > 0 and magicien.vie > 0:
            if roi_sorcier.tour == 'joueur1':
                p.print_lbl(f"⏩ {roi_sorcier.nom} commence !")
                degats = roi_sorcier.frapper(magicien.nom, roi_sorcier.degats)
                exp_recue = magicien.hit_or_miss(degats, roi_sorcier.nom)
                roi_sorcier.gagne_experience(exp_recue)
                if magicien.vie <= 0:
                    break
                p.print_lbl(f"⏪ {magicien.nom} riposte !")
                degats = magicien.frapper(roi_sorcier.nom, magicien.degats)
                exp_recue = roi_sorcier.hit_or_miss(degats, magicien.nom)
                magicien.gagne_experience(exp_recue)
            else:
                p.print_lbl(f"⏩ {magicien.nom} commence !")
                degats = magicien.frapper(roi_sorcier.nom, magicien.degats)
                exp_recue = roi_sorcier.hit_or_miss(degats, magicien.nom)
                magicien.gagne_experience(exp_recue)
                if roi_sorcier.vie <= 0:
                    break
                p.print_lbl(f"⏪ {roi_sorcier.nom} riposte !")
                degats = roi_sorcier.frapper(magicien.nom, roi_sorcier.degats)
                exp_recue = magicien.hit_or_miss(degats, roi_sorcier.nom)
                roi_sorcier.gagne_experience(exp_recue)
            turnNumber += 1
            p.print_lbl(f"------------------------------------")
            p.print_lbl(f"Tour {turnNumber} :\n{roi_sorcier.nom} a {roi_sorcier.vie} PV et {magicien.nom} a {magicien.vie} PV.")
            p.print_lbl(f"EXP Actuelles : {roi_sorcier.experience} EXP pour {roi_sorcier.nom} et {magicien.experience} EXP pour {magicien.nom}.")
            p.print_lbl(f"-----------------")
            
        p.print_lbl(f"Le combat est terminé ! ✋\n{roi_sorcier.nom} a {roi_sorcier.vie} PV et {magicien.nom} a {magicien.vie} PV.")
        p.print_lbl(f"Le combat a duré {turnNumber} tours.")




# # Variables definitions
# choicesKeys = ["pi", "pa", "ci"]
# choices = [("pi", "la Pierre"), ("pa", "le Papier"), ("ci", "les Ciseaux")]
# choicesDict = dict(choices)
# isGameRunning = True
# playerScore = 0
# opponentScore = 0

# # Game
# def intro() -> None:
#     """Small text of introduction
#     """
#     p.print_lbl("Bienvenue dans le jeu exceptionnel de Pierre-Papier-Ciseaux !\n")
#     p.print_lbl("Ce jeu fait rêver petits et grands. Alors vous aussi sans doute...hein ?\n")
#     p.print_lbl("Rappel des règles : Pierre✊ bat Ciseaux✌ , Ciseaux✌ bat Papier✋ , Papier🤚 bat Pierre✊.\n")
#     p.print_lbl("Vous allez jouer avec l'ordinateur. Que la chance soit avec vous !\n")
    
# def game() -> None:
#     """To run the game
#     """
#     global isGameRunning
#     global playerScore
#     global opponentScore

#     while isGameRunning:
#         playerChoice = player.choice(choicesKeys)
#         if playerChoice == "q":
#             showScores(isLastTime=True)
#             isGameRunning = False
#         else:
#             opponentChoice = opponent.choice(choicesKeys)
#             whoWins(playerChoice, opponentChoice)

# def whoWins(playerChoice: str, opponentChoice: str) -> None:
#     """To define who won the round

#     Args:
#         playerChoice (str): choice made by the player
#         opponentChoice (str): choice made by the opponent
#     """
#     global playerScore
#     global opponentScore
#     global choicesDict
#     global choicesKeys
        
#     if playerChoice == opponentChoice:
#         p.print_lbl(f"Vous avez tous les deux choisis {choicesDict[playerChoice]} ! C'est une égalité !\n")
#     elif (playerChoice == choicesKeys[0] and opponentChoice == choicesKeys[2]) or (playerChoice == choicesKeys[1] and opponentChoice == choicesKeys[0]) or (playerChoice == choicesKeys[2] and opponentChoice == choicesKeys[1]):
#         playerScore += 1
#         p.print_lbl(f"✅ Vous avez gagné un point ! L'ordi avait choisi {choicesDict[opponentChoice]} et vous l'avez battu avec {choicesDict[playerChoice]} !\n")
#     else:
#         opponentScore += 1
#         p.print_lbl(f"❌ Perdu ! Vous avez choisi {choicesDict[playerChoice]} et l'ordi vous a battu avec {choicesDict[opponentChoice]}...\n")
#     showScores()
#     return
    
# def showScores(isLastTime: bool = False) -> None:
#     """To show the current scores

#     Args:
#         isLastTime (bool, optional): if True, adds text. Defaults to False.
#     """
#     if isLastTime:
#         p.print_lbl("Scores finaux :")
#     p.print_lbl(f"Votre score : {playerScore} | Score de l'ordi : {opponentScore}\n")