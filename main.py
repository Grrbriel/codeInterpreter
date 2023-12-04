import A_lexico as lexi
import A_sintatico as sint

inputX = input("input:")

lexi.set_input(inputX)
lexi.tokenizer()

lexOutput = lexi.get_lexOutput()
print(lexOutput)

sint.sint(inputX)

