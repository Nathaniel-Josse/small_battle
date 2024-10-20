from Lib.custom import printlbl as p
from Lib.classes.personnage import Personnage
import random as r
import math as m

class Magicien(Personnage):
    
    def __init__(self, nom: str, vie: int, degats: int, experience: int, expRate: float, tour: str) -> None:
        super().__init__(nom, vie, degats, experience, expRate, tour)
    
    def frapper(self, cible: str, degats: int) -> int:
            randomMove = r.randint(1, 2)
            if randomMove == 1:
                p.print_lbl(f"🧊 {self.nom} lance une boule de glace sur {cible} !")
                return degats * 2 + self.experience
            else:
                p.print_lbl(f"➰ {self.nom} teste {cible} en envoyant un faux sort pour augmenter sa future expérience !")
                exp_rate_increase = r.randint(1, 100) / 50
                self.exp_rate += exp_rate_increase
                p.print_lbl(f"⏫ {self.nom} a augmenté son taux d'expérience de {self.exp_rate - exp_rate_increase:.2f} à {self.exp_rate:.2f} !")
                return degats     
            
    def hit_or_miss(self, degats: int, envoyeur: str) -> int:
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
        exp_gagnee = m.ceil(exp_recue * self.exp_rate)
        self.experience += exp_gagnee
        p.print_lbl(f"🔼 {self.nom} a gagné {exp_gagnee} points d'expérience !")