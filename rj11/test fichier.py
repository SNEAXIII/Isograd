eol = "\n"
with open("a_tester.txt","r") as f:
    liste_a_tester = f"lines = {f.read().split(eol)}"
print(liste_a_tester)

