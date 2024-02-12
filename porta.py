# on retourne la clé de chiffrage en fonction de la longueur de la phrase à déchiffrer
def definirCle(longueur,key):
    q = longueur // len(key)
    r = longueur % len(key)
    result = ""
    for i in range(q):
        result=result + key
    result = result + key[0:r]
    return result
# on code la phrase à chiffrer par l'algorithme de Porta avec la clé de chiffrage
def porta(phraseAChiffrer,cleChiffrage):
    phraseChiffree = ""
    phraseAChiffrer = phraseAChiffrer.lower()
    phraseCle = definirCle(len(phraseAChiffrer),cleChiffrage)
    # on lit tous les caractères de la phrase à chiffrer
    for i in range(len(phraseAChiffrer)):
        # si c'est une lettre on va calculer la lettre correspondante avec la clé
        if ord("a") <= ord(phraseAChiffrer[i]) <= ord("z"):
            lettrePhraseCle = phraseCle[i]
            lettreChiffree = subsitueLettre(phraseAChiffrer[i],tupleAlphabet[posElement(lettrePhraseCle) - 1]).lower()           
            phraseChiffree = phraseChiffree + lettreChiffree
        # sinon on laisse le caractère
        else:
            phraseChiffree = phraseChiffree + phraseAChiffrer[i]  
    return phraseChiffree 
# retourne le numéro de l'alphabet à utiliser
# AB => 1 , CD => 2 , ... , YZ => 13
def posElement(lettre):
    x = ord(lettre.upper()) - 64 
    # pair
    if x % 2 == 0:
        return x // 2
    # impair
    else:
        return x // 2 + x % 2
# on retourne la lettre chiffrée en fonction de l'alphabet de chiffrage
def subsitueLettre(lettre,alphabet):
    lettre = lettre.upper()
    # on sépare l'alphabet en deux parties égales
    alpha1 = alphabet[0:13]
    alpha2 = alphabet[13:26] 
    alphaLecture = ""
    alphaRetour = ""
    # on vérifie  si la lettre est dans alpha1 ou alpha2
    position = -1
    i = 0 
    while (i < len(alpha1)):
        if alpha1[i] == lettre:
            position = i
            i = 99
        i = i + 1
    # lettre est dans alpha1 on connait sa position 
    if position != -1 :
        alphaLecture = alpha1
        alphaRetour = alpha2
    else:
        # lettre est dans alpha2 on cherche sa position
        alphaLecture = alpha2
        alphaRetour = alpha1
        i = 0 
        while i < len(alphaLecture):
            if alphaLecture[i] == lettre:
                position = i
                i = 99
            i = i + 1
    return alphaRetour[position]   
# Main Script
tupleAlphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMZNOPQRSTUVWXY","ABCDEFGHIJKLMYZNOPQRSTUVWX","ABCDEFGHIJKLMXYZNOPQRSTUVW","ABCDEFGHIJKLMWXYZNOPQRSTUV",
                 "ABCDEFGHIJKLMVWXYZNOPQRSTU","ABCDEFGHIJKLMUVWXYZNOPQRST","ABCDEFGHIJKLMTUVWXYZNOPQRS","ABCDEFGHIJKLMSTUVWXYZNOPQR","ABCDEFGHIJKLMRSTUVWXYZNOPQ",
                 "ABCDEFGHIJKLMQRSTUVWXYZNOP","ABCDEFGHIJKLMPQRSTUVWXYZNO","ABCDEFGHIJKLMOPQRSTUVWXYZN")
print("------------------------")
print("------ Code PORTA ------")
print("------------------------")
phrase = input("Quelle est la phrase à coder ? ")
cle = input("Quelle est la clé de codage ? ")
print("La phrase chiffrée est :")
print("{}".format(porta(phrase,cle)))