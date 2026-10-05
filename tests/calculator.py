class Calculator:
    """Минимальная бизнес-логика, перенесенная из лабораторной работы 6."""

    def add(self, left, right):
        return left + right

    def divide(self, left, right):
        if right == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return left / right
