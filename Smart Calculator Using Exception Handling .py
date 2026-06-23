
# ── Smart Calculator with try/except ──────────────────

def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ❌ Not a number. Try again.")


def calculate(a, op, b):
    """Perform the operation and handle all errors."""
    try:
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        elif op == "**":
            result = a ** b
        elif op == "%":
            if b == 0:
                raise ZeroDivisionError("Cannot mod by zero")
            result = a % b
        else:
            raise ValueError(f"Unknown operator: {op}")

    except ZeroDivisionError as e:
        print(f"  ❌ Math error: {e}")
        return None

    except ValueError as e:
        print(f"  ❌ Input error: {e}")
        return None

    except OverflowError:
        print("  ❌ Result too large to compute!")
        return None

    else:
        print(f"  ✅ Result: {result}")
        return result

    finally:
        print("  ── calculation finished ──")


def main():
    print("🧮 Smart Calculator")
    history = []

    while True:
        print("\nOperators: + - * / ** %  |  type 'history' or 'quit'")

        try:
            raw = input("Enter expression (e.g. 10 / 2): ").strip()

            if raw == "quit":
                print("Bye! 👋")
                break

            if raw == "history":
                print("\n".join(history) if history else "No history yet.")
                continue

            parts = raw.split()           # e.g. ["10", "/", "2"]
            if len(parts) != 3:
                raise SyntaxError("Use format: number operator number")

            a = float(parts[0])
            op =        parts[1]
            b = float(parts[2])

        except SyntaxError as e:
            print(f"  ❌ Format error: {e}")
            continue

        except ValueError:
            print("  ❌ Numbers only on left and right.")
            continue

        result = calculate(a, op, b)
        if result is not None:
            history.append(f"{a} {op} {b} = {result}")


main()
