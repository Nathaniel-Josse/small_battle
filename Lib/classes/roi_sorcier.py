from Lib.custom import printlbl as p
from Lib.classes.personnage import Personnage
import random as r
import math as m

class RoiSorcier(Personnage):
    
    def __init__(self, nom: str, vie: int, degats: int, experience: int, expRate: float, tour: str) -> None:
        super().__init__(nom, vie, degats, experience, expRate, tour)
    
    def frapper(self, cible: str, degats: int) -> int:
        randomMove = r.randint(1, 2)
        # Frappe 1 : dégâts * 2 + expérience
        if randomMove == 1:
            p.print_lbl(f"🔥 {self.nom} lance une boule de feu sur {cible} !")
            return degats * 2 + self.experience
        # Frappe 2 : dégâts * (1 + expérience * 0.2).
        # Seuils :
        # 0-5 EXP : multiplication par 1.0 - 2.0
        # 6-10 EXP : multiplication par 2.2 - 3.0
        # etc.
        else:
            p.print_lbl(f"👀 {self.nom} lance un sort de connaissance sur {cible} !")
            return m.ceil(degats * (1 + self.experience * 0.2))      
        
    def hit_or_miss(self, degats: int, envoyeur: str) -> int:
        # 85% de chance de toucher
        if r.randint(1, 100) > 15:
            self.recoit_degats(degats, envoyeur)
            return 1
        else:
            self.esquive()
            return 0
    
    def esquive(self) -> None:
        p.print_lbl(f"💨 {self.nom} a esquivé l'attaque !")
    
    def recoit_degats(self, degats: int, envoyeur: str) -> None:
        self.vie = self.vie - degats
        p.print_lbl(f"💥 {self.nom} a subi {degats} points de dégâts à cause de {envoyeur} !")
    
    def gagne_experience(self, exp_recue: int) -> None:
        # Exp gagnée = exp reçue * taux d'expérience. Arrondi supérieur.
        exp_gagnee = m.ceil(exp_recue * self.exp_rate)
        self.experience += exp_gagnee
        p.print_lbl(f"🔼 {self.nom} a gagné {exp_gagnee} points d'expérience !")