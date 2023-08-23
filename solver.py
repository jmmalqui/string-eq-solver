WHITESPACE = " "
OPERATORS = "^/*-%+"
OPENBRACKET = "("
CLOSEBRACKET = ")"


def solve_eq(expression: str):
    """Evaluates a mathematical expression with the following operators.\n
    "+" (addition) "-" (substraction) "*" (multiplication) "/" (division) "^" (pow) "%" (modulo).\n
    Example: (3 + 2) + (4 * (5 + 3)) = 37
    """
    index = 0
    start_parse = True
    buffer = ""
    ob_id = None
    bracket_level = 0
    while True:
        char = expression[index]
        if char == OPENBRACKET:
            buffer = ""
            bracket_level += 1
            if expression[index + 1] == OPENBRACKET:
                index += 1
                start_parse = False
                continue
            else:
                ob_id = index
                index += 1
                start_parse = True
                continue
        if start_parse:
            if char == CLOSEBRACKET:
                bracket_level -= 1
                start_parse = False
                expression = __delsubstr(expression, ob_id - 1, f"({buffer})")
                if expression == "":
                    break
                else:
                    expression = __fillstr(
                        expression, ob_id - 1, str(__solve_no_brackets(buffer))
                    )
                index -= len(buffer) + 3
                buffer = ""
                continue
            buffer += char
        index += 1
        if index == len(expression):
            assert bracket_level == 0, "Parenthesis do not match"
            if buffer:
                break
            else:
                index = 0
                start_parse = True
                continue

    return __solve_no_brackets(buffer)


def __solve_no_brackets(expression: str) -> float:
    number_list = []
    operator_list = []
    on_parsing_number = ""
    fully_parsed_number = ""
    should_continue_parse = True
    left_operand = None
    right_operand = None
    operator = None
    index = 0
    end_of_expression = False
    while True:
        char = expression[index]
        if char == WHITESPACE:
            index += 1
            continue
        if index == len(expression) - 1:
            on_parsing_number += char
            end_of_expression = True
        if char in OPERATORS or index == len(expression) - 1:
            should_continue_parse = False
            fully_parsed_number = on_parsing_number
            if left_operand:
                right_operand = fully_parsed_number
            if not left_operand:
                left_operand = fully_parsed_number
            if left_operand and right_operand and operator:
                left_operand = fully_parsed_number
                right_operand = None
                operator_list.append(operator)
            operator = char
            on_parsing_number = ""
            number_list.append(float(fully_parsed_number))
        else:
            should_continue_parse = True
        if end_of_expression:
            break
        if should_continue_parse:
            on_parsing_number += char
        index += 1
    used_operators = list(set(operator_list))
    for operator in OPERATORS:
        if operator not in used_operators:
            continue
        else:
            __solve_iterate_for_operator(operator, number_list, operator_list)
    return number_list[0]


def __solve_iterate_for_operator(
    operator: str, expression_number_list: list, expression_operator_list: list
):
    pointer = 0
    while True:
        pair = [expression_number_list[pointer], expression_number_list[pointer + 1]]
        if expression_operator_list[pointer] != operator:
            pointer += 1
            if pointer == len(expression_number_list) - 1:
                break
        else:
            result = __reduce_pair(pair[0], pair[1], operator)
            expression_number_list.pop(pointer)
            expression_number_list.pop(pointer)
            expression_operator_list.pop(pointer)
            expression_number_list.insert(pointer, result)
            if pointer == len(expression_number_list) - 1:
                break


def __reduce_pair(num1: float, num2: float, operator: str):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    if operator == "^":
        return num1**num2
    if operator == "%":
        return num1 % num2
    else:
        return f"{operator} operator not recognized"


def __delsubstr(string: str, index: int, substr: str):
    l_string = list(string)
    pointer = 0
    while True:
        if l_string[index + 1] == substr[pointer]:
            l_string.pop(index + 1)
        pointer += 1
        if pointer == len(substr):
            break
    string = "".join(l_string)
    return string


def __fillstr(string: str, index: int, filling: str):
    l_string = list(string)
    pointer = index
    while True:
        l_string.insert(pointer + 1, filling[pointer - index])
        pointer += 1
        if pointer - index == len(filling):
            break
    string = "".join(l_string)
    return string
