from menuBot import goto_menu
import random
activeGames = {}


def newGame(chatID, newGame):
    activeGames.update({chatID: newGame})
    return newGame

def getGame(chatID):
    return activeGames.get(chatID)

def stopGame(chatID):
    activeGames.pop(chatID)



class GameRPS:
    values = ["Камень", "Ножницы", "Бумага"]
    def __init__(self):
        self.computerChoice = self.__class__.getRandomChoice()

    @classmethod
    def getRandomChoice(cls):
        lenValues = len(cls.values)
        import random
        rndInd = random.randint(0, lenValues - 1)
        return cls.values[rndInd]

    def playerChoice(self, player1Choice):
        winner = None
        code = player1Choice[0] + self.computerChoice[0]
        if player1Choice == self.computerChoice:
            winner = "Ничья!"
        elif code == "КН" or code == "БК" or code == "НБ":
            winner = "Молодец, ты победил!"
        else:
            winner = "Ха-ха, я выиграл!"
        return f"{player1Choice} vs {self.computerChoice} = " + winner



class Dice:

    dice = [1, 2, 3, 4, 5, 6]

    def __init__(self):
        self.computerChoice = self.__class__.getRandomDice()
        self.player1Choice = self.__class__.getRandomDice()

    @classmethod
    def getRandomDice(cls):
        lenValues = len(cls.dice)
        rndInd = random.randint(0, lenValues - 1)
        return cls.dice[rndInd]

    def playerChoice(self):
        winner = None
        if self.player1Choice == self.computerChoice:
            winner = "Ничья!"
        elif self.player1Choice > self.computerChoice:
            winner = "Тебе свезло, ты выиграл"
        else:
            winner = "Хе-хе, весёлый Роджер сегодня улыбнулся мне, я выиграл)"
        return f"{self.player1Choice} vs {self.computerChoice} = " + winner



def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text
    if ms_text in GameRPS.values:
        gameRSP = getGame(chat_id)
        if gameRSP is None:
            goto_menu(bot, chat_id, "Выход")
            return
        text_game = gameRSP.playerChoice(ms_text)
        bot.send_message(chat_id, text=text_game)
        gameRSP.newGame()

