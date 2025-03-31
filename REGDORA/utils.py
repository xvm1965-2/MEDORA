# REGDORA/utils.py
def get_clean_verbose_name(field):
    """
    Extracts the clean verbose name by removing the field code in brackets
    Example: "Autorità competente (B_01.01.0050)" → "Autorità competente"
    """
    verbose_name = field.verbose_name
    if '(' in verbose_name and ')' in verbose_name:
        return verbose_name.split('(')[0].strip()
    return verbose_name

def validate_lei(value):
    """
    Validate the LEI (Legal Entity Identifier) according to ISO 17442:
    - Must be 20 characters (uppercase letters A-Z and digits 0-9)
    - First 18 characters: Any alphanumeric (A-Z, 0-9)
    - Last 2 characters: Check digits (must pass Modulus 97 test)
    """
    # Ensure correct format (20 characters, uppercase letters and digits only)
    if not re.fullmatch(r'^[0-9A-Z]{18}[0-9]{2}$', value):
        raise ValidationError(_("Il codice LEI deve essere lungo 20 caratteri e composto solo da lettere maiuscole e cifre."))

    # Convert letters to numbers (A=10, B=11, ..., Z=35)
    converted_value = ''.join(str(int(c, 36)) for c in value)

    # Modulus 97 check
    if int(converted_value) % 97 != 1:
        raise ValidationError(_("Il codice LEI non è valido secondo la norma ISO 17442 (fallito controllo Modulo 97)."))
