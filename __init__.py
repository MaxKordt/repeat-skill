from mycroft import MycroftSkill, intent_file_handler


class Repeat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('repeat.answers.intent')
    def handle_repeat(self, message):
        self.speak_dialog("repeat.answers")


def create_skill():
    return Repeat()

