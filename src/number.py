import re

def is_nan(string):
    return string != string


def format_value(element):
    # A value was found with incorrect formatting. (3,045.99 instead of 3045.99)
    if is_nan(element):
        return 0.0
    if type(element) == str:
        if "." in element and "," in element:
            element = element.replace(".", "").replace(",", ".")
        elif "," in element:
            element = element.replace(",", ".")
        element = re.sub(r"^\s*-\s*$", "0.0", element)
    if "R$" in str(element):
        element = element.replace("R$", "")
    if " " in str(element):
        element = element.replace(" ", "")
    if "-" in str(element):
        # Remove o símbolo - APÓS o número
        # MPES faz isso, e.g. "399.00-"
        element = re.sub(r"(?<=\d)-\s*", "", str(element))
    if str(element).count('.') > 1:
        # Para casos como 3.999.90 -> 3999.90
        element = str(element).replace('.', '', 1)

    return float(element)