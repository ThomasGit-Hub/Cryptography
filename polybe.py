def short_mdp(mdp):
    short_mdp = []
    for letter in mdp:
        if letter not in short_mdp:
            short_mdp.append(letter)
    return short_mdp
def create_grid(mdp, alphabet):
    pre_grid = []
    ligne = []
    grid = []
    for e in mdp:
        pre_grid.append(e)
    for letter in alphabet:
        if letter not in pre_grid:
            pre_grid.append(letter)
    for ele in pre_grid:
        if len(ligne) == 5:
            grid.append(ligne)
            ligne = []
            ligne.append(ele)
        else:
            ligne.append(ele)
    return grid      
def create_message(grid, message):
    crpt_message = []
    for letter in message:
        if letter == "j":
            for e in range(2):
                crpt_message.append(str(0))
        elif letter == "." or letter == "?" or letter == "," or letter == "!" or letter == "/" or letter == " ":
            crpt_message.append(letter)
        else:
            for ligne in grid:
                for col in ligne:
                    if letter == col:
                        crpt_message.append(str(grid.index(ligne) + 1))
                        crpt_message.append(str(ligne.index(col) + 1))
    return crpt_message
print("")
print("-------------------------")
print("------ Code POLYBE ------")
print("-------------------------")
password = str(input("Entrez votre mot de passe (j exclus) "))
alphabet = "abcdefghiklmnopqrstuvwxyzj"
message = str(input("Quel est le message à encoder "))
print("La phrase chiffrée est :")
print(''.join(create_message(create_grid(short_mdp(password), alphabet), message)))