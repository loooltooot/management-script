def multiply_array_elements(array):
    summa = 1
    for item in array:
        summa *= item

    return summa

def print_deltas(plan, fact):
    absolute = fact - plan
    relative = round((fact / plan * 100), 2)

    print(f'Absolute delta = {absolute}')
    print(f'Relative delta = {relative}%')

def chain_method(plan, fact):
    delta, multiply = 0, multiply_array_elements(plan)
    for i in range(3):
        plan[i] = fact[i]

        previous_multiplay = multiply
        multiply = multiply_array_elements(plan)
        delta = multiply - previous_multiplay

        print(f'XYZ{i} = {multiply} - {previous_multiplay} = {delta}')

def main():
    plan, fact = [], [] 

    for i in range(3):
        plan.append(float(input(f'Enter {i} var of plan: ')))

    for i in range(3):
        fact.append(float(input(f'Enter {i} var of fact: ')))

    plan_multiply = multiply_array_elements(plan)
    fact_multiply = multiply_array_elements(fact)

    print_deltas(plan_multiply, fact_multiply)

    chain_method(plan, fact)

if __name__ == '__main__':
    main()