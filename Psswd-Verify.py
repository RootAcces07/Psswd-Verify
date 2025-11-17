import string

SPECIAL_CHARS = set("@#€%&*!$?_-+<>")

# Utiliser input() au lieu de getpass.getpass() pour que le mot de passe soit visible lors de la saisie
pwd = input("Entrez un mot de passe : ").strip()

is_long = len(pwd) >= 8
has_upper = any(c.isupper() for c in pwd)
has_lower = any(c.islower() for c in pwd)
has_digit = any(c.isdigit() for c in pwd)
has_special = any(c in SPECIAL_CHARS for c in pwd)

checks = {
    "longueur >= 8": is_long,
    "une lettre majuscule": has_upper,
    "une lettre minuscule": has_lower,
    "un chiffre": has_digit,
    "un caractère spécial": has_special,
}

if all(checks.values()):
    print("Mot de passe FORT ✅")
else:
    print("Mot de passe FAIBLE ❌")
    print("Il vous manque :")
    for desc, ok in checks.items():
        if not ok:
            print(f" - {desc}")
