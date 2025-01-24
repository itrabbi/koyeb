import random


def luhn_check(card_number):

    card_digits = [int(digit) for digit in str(card_number)][::-1] 
    for i in range(1, len(card_digits), 2):  
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] -= 9
    total_sum = sum(card_digits)
    return total_sum % 10 == 0


def cc_gen(
    cc,
    mes="x",
    ano="x",
    cvv="x",
    amount="x",
):
    if amount != "x":
        amount = int(amount)
    else:
        amount = 10
    genrated = 0
    ccs = []
    while genrated < amount:
        genrated += 1
        s = "0123456789"
        l = list(s)
        random.shuffle(l)
        result = "".join(l)
        result = cc + result

        if cc[0] == "3":
            ccgen = result[0:15]
        else:
            ccgen = result[0:16]

        while not luhn_check(ccgen):
            random.shuffle(l)
            result = "".join(l)
            result = cc + result
            if cc[0] == "3":
                ccgen = result[0:15]
            else:
                ccgen = result[0:16]

        if mes == "x":
            mesgen = random.randint(1, 12)
            if len(str(mesgen)) == 1:
                mesgen = "0" + str(mesgen)
        else:
            mesgen = mes
        if ano == "x":
            anogen = random.randint(2024, 2030)
        else:
            anogen = ano
        if cvv == "x":
            if cc[0] == "3":
                cvvgen = random.randint(1000, 9999)
            else:
                cvvgen = random.randint(100, 999)
        else:
            cvvgen = cvv

        lista = (
            "<code>"
            + str(ccgen)
            + "|"
            + str(mesgen)
            + "|"
            + str(anogen)
            + "|"
            + str(cvvgen)
            + "</code>"
        )
        ccs.append(lista)
    return ccs
