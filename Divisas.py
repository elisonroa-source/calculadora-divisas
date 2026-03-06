def exchange_money(budget, exchange_rate):
    """
    Convierte dinero usando una tasa de cambio
    """
    return budget / exchange_rate


def main():
    print("Calculadora de Divisas")

    budget = float(input("Ingrese su presupuesto en USD: "))
    exchange_rate = float(input("Ingrese la tasa de cambio: "))

    resultado = exchange_money(budget, exchange_rate)

    print("Dinero convertido:", resultado)


if __name__ == "__main__":
    main()