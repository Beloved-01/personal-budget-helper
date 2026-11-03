def budget_remaining(budget, food, transport):
    return budget - food - transport


def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining."


result = budget_remaining(2000, 900, 600)
print(budget_message("Ada", result))

result2 = budget_remaining(1500, 0, 0)
print(budget_message("Ada", result2))

result3 = budget_remaining(1000, 800, 500)
print(budget_message("Ada", result3))
