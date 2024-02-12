def reverse_and_encrypt(message):
    lsMessage = list(message)
    ls_reverse = lsMessage[::-1]
    result = []
    for letter in range(len(lsMessage)):
        result.append(lsMessage[letter])
        result.append(ls_reverse[letter])    
    return result[:len(lsMessage)]  
# programme principal
message = input("Please enter your message")
print("----------------------------")
print("------ Code DEBUT FIN ------")
print("----------------------------")
print("La phrase chiffrée est :")
print(''.join(reverse_and_encrypt(message)))