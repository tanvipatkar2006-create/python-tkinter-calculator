from calculator import Calculator

def repl():
    calc = Calculator()
    print("CLI Calculator — type 'help' for commands, 'exit' to quit.")
    while True:
        try:
            raw = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye."); break

        if not raw: continue
        if raw.lower() in ("exit","quit"): break
        if raw.lower() == "help":
            print("Commands: add a b | sub a b | mul a b | div a b | pow a b | pct a b | neg a")
            continue

        parts = raw.split()
        cmd, args = parts[0].lower(), parts[1:]
        try:
            if cmd == "add": print(calc.add(float(args[0]), float(args[1])))
            elif cmd == "sub": print(calc.subtract(float(args[0]), float(args[1])))
            elif cmd == "mul": print(calc.multiply(float(args[0]), float(args[1])))
            elif cmd == "div": print(calc.divide(float(args[0]), float(args[1])))
            elif cmd == "pow": print(calc.power(float(args[0]), float(args[1])))
            elif cmd == "pct": print(calc.percent(float(args[0]), float(args[1])))
            elif cmd == "neg": print(calc.negate(float(args[0])))
            else: print("Unknown command")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
