import main as program

while True:
    console = input("$stateZ > ")
    if console.strip() == "": continue
    result, error = program.run("<console>", console)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))