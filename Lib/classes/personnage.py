from abc import ABC, abstractmethod

class Personnage(ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Personnage:
            raise TypeError("Personnage class may not be instantiated")
        return object.__new__(cls)
    
    def __init__(self, nom, vie, frappes, experience, degats, tour):
        self.__nom = nom
        self.__vie = vie
        self.__frappes = frappes
        self.__experience = experience
        self.__degats = degats
        self.tour = tour

    @abstractmethod
    def frapper(self):
        pass
    
    @abstractmethod
    def esquive(self):
        pass
    
    @abstractmethod
    def recoit_degats(self):
        pass
