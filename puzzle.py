from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

def exclusive_or(symbol0, symbol1):
    """simple helper method for exclusive or"""
    return And(Or(symbol0, symbol1), Not(And(symbol0, symbol1)))

# pairs of knights and knaves for use with convenience function 'character_says' below
A = (AKnight, AKnave)
B = (BKnight, BKnave)
C = (CKnight, CKnave)

def character_says(knight_knave_pair, sentence):
    """Convenience function to represent knowledge of statements by knight/knave characters.
       Generates a conjunction of the knight implication and the knave implication for the given sentence.
       Pass either A,B or C as the knight_knave_pair who said it, and the sentence they said.
       e.g.
       character_says(A,some_sentence) will generate:
       And(
         Implication(AKnight, some_sentence),
         Implication(AKnave, Not(some_sentence))
       )
    """
    knight = knight_knave_pair[0]
    knave = knight_knave_pair[1]
    return And(Implication(knight, sentence), Implication(knave, Not(sentence)))

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    #
    # General Knights and Knaves Problem Structure
    #

    # A is either a Knight or a Knave
    exclusive_or(AKnight, AKnave),
    #
    # Specific Character statements for this puzzle
    #

    # A says "I am both a knight and a knave."
    character_says(A, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    #
    # General Knights and Knaves Problem Structure
    #

    # A is either a Knight or a Knave
    exclusive_or(AKnight, AKnave),
    # B is either a Knight or a Knave
    exclusive_or(BKnight, BKnave),

    #
    # Specific Character statements for this puzzle
    #

    # A says "We are both knaves."
    character_says(A, And(AKnave, BKnave))

    # B says nothing.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    #
    # General Knights and Knaves Problem Structure
    #

    # A is either a Knight or a Knave
    exclusive_or(AKnight, AKnave),
    # B is either a Knight or a Knave
    exclusive_or(BKnight, BKnave),

    #
    # Specific Character statements for this puzzle
    #

    # A says "We are the same kind."
    character_says(A, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # B says "We are of different kinds."
    character_says(B, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

    #
    # General Knights and Knaves Problem Structure
    #

    # A is either a Knight or a Knave
    exclusive_or(AKnight, AKnave),
    # B is either a Knight or a Knave
    exclusive_or(BKnight, BKnave),
    # C is either a Knight or a Knave
    exclusive_or(CKnight, CKnave),

    #
    # Specific Character statements for this puzzle
    #

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Or(character_says(A, AKnight), character_says(A, AKnave)),

    # B says "A said 'I am a knave'."
    character_says(B, character_says(A, AKnave)),

    # B says "C is a knave."
    character_says(B, CKnight),

    # C says "A is a knight."
    character_says(C, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
