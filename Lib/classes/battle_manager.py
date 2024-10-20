from Lib.classes.roi_sorcier import RoiSorcier
from Lib.classes.magicien import Magicien
from Lib.custom import printlbl as p
import random as r

class BattleManager():
    
    def launch(self) -> None:
        rs_pv = 100
        m_pv = 100
        rs_degats = 10 + r.randint(-2, 2)
        m_degats = 10 + r.randint(-2, 2)
        base_experience = 0
        exp_rate_1 = 1 + (r.randint(0, 5) / 10)
        exp_rate_2 = 1 + (r.randint(0, 5) / 10)
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
    def battle(roi_sorcier: RoiSorcier, magicien: Magicien) -> None:
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