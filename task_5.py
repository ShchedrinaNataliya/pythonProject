from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

nouns = choice(nouns)
adverbs = choice(adverbs)
adjectives = choice(adjectives)
joke = f'{nouns} {adverbs} {adjectives}'
print(joke)

# Не получается в функцию завернуть