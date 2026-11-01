"""Buzzword-generator uit het werkboek (Scripting 4: Change Management via CI/CD).

Dit is de code uit het werkboek, maar opgeschoond na de stap
"Improve your code" (flake8): de functionaliteit is precies hetzelfde.
"""
from __future__ import print_function  # overblijfsel uit Python 2, doet niets in Python 3

import random

# Woordenlijsten (tuples) waaruit de zin wordt opgebouwd
buzz = ('continuous testing', 'continuous integration',
        'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
           'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')


def sample(lijst, n=1):
    """Kies n willekeurige, VERSCHILLENDE elementen uit lijst.

    Bij n == 1 krijg je het element zelf terug (geen lijst).
    """
    result = random.sample(lijst, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    """Maak een buzzword-zin van (minstens) 5 woorden, met hoofdletters."""
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
                       sample(verbs), buzz_terms[1]])
    return phrase.title()


if __name__ == "__main__":
    print(generate_buzz())
