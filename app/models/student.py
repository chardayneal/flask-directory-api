from .ada_member import AdaMember

class Student(AdaMember):
    def __init__(self, id, name, pronouns, personality, fun_fact="I'm not fun"):
        super().__init__(id, name, pronouns, personality)
        self.fun_fact = fun_fact
