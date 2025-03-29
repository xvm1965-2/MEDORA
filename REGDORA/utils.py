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