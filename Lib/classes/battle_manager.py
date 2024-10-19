from Lib.classes.roi_sorcier import RoiSorcier
from Lib.classes.magicien import Magicien
from Lib.custom import printlbl as p

class BattleManager():
    pass    




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