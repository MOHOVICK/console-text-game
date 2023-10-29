"""
Автор: Никита Моховиков (aka MOHOVICK)
GitHub: https://github.com/MOHOVICK
ВКонтакте: https://vk.com/m0h0vick
"""

import sys
from story import story
from pick import pick

def get_main_text(index: int) -> str:
    "Получение главного текста"
    return story["story_line"][index]["text"]

def get_actions_text(index: int) -> []:
    "Получение вариантов ответа"
    return [i["text"] for i in story["story_line"][index]["actions"]]

def get_next_action(index: int, select_action: int):
    "Получение ID следующего действия"
    action = story["story_line"][index]["actions"][select_action]["next"]
    if "ending" in str(action):
        display_ending(story["endings"][action]["text"])
    else:
        return action

def show_text(text_index: int):
    title = get_main_text(text_index)
    options = get_actions_text(text_index)
    option, index = pick(options, title, indicator="=>")
    show_text(get_next_action(text_index, index))

def display_ending(text: str):
    options = [
        "Сыграть ещё раз!",
        "Выйти"
    ]
    option, index = pick(options, text, indicator="=>")
    match (index):
        case 0:
            show_text(0)
        case 1:
            sys.exit()

def main():
    show_text(0)

if __name__ == "__main__":
    main()