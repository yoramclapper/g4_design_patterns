from abc import ABC, abstractmethod


class Spell(ABC):

    @property
    @abstractmethod
    def spell_name(self) -> str:
        pass


class AbracadabraSpell(Spell):

    @property
    def spell_name(self):
        return "Abracada"
