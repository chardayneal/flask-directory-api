from .ada_member import AdaMember

class Instructor(AdaMember):
    def __init__(self, id, name, pronouns, personality, favorite_language=None):
        super().__init__(id, name, pronouns, personality)
        self.favorite_language = favorite_language if favorite_language else "All"

