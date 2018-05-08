# -*- coding: utf-8 -*-
from src import bot


def main():
    token = open("token.txt", "r").read()
    receiptor_bot = bot.Bot(token)
    receiptor_bot.run()


if __name__ == '__main__':
    main()
