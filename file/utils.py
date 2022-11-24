

def convert_type(str):
    if str == "1":
        return "Débito"
    elif str == "2":
        return "Boleto"
    elif str == "3":
        return "Financiamento"
    elif str == "4":
        return "Crédito"
    elif str == "5":
        return "Recebimento Empréstimo"
    elif str == "6":
        return "Vendas"
    elif str == "7":
        return "Recebimento TED"
    elif str == "8":
        return "Recebimento DOC"
    elif str == "9":
        return "Aluguel"

def calculate_total(files):
    total = 0
    for file in files:
        if file.tipo == "Boleto" or file.tipo == "Financiamento" or file.tipo == "Aluguel":
            total -= float(file.valor)
        else:
            total += float(file.valor)
    return round(total, 2)