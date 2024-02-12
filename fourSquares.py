def Grid(cle):
    '''Here we create a grid in a 5x5 format. The letter j is excluded from the grid.'''
    grid=[]
    alpahabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count=0
    for i in range(5):
        line=[]
        if cle != 0:
            for lettres in cle:
                if lettres not in line:
                    line.append(lettres)
            while len(line)<=4:
                if alpahabet[count] not in line:
                    line.append(alpahabet[count])
                count+=1
            cle=0
            grid.append(line)
        else:
            while len(line)<=4:
                if alpahabet[count] not in grid[0]:
                    line.append(alpahabet[count])
                count+=1
            grid.append(line)
    return grid
def Square(grid1,grid2,grid3,grid4,message):
    '''We create a tab with four grids previously created with the grid() function.'''
    shortened_message="" 
    shrt_message_encrypted=""
    final_message=""
    count=0 
    odd=False
    for letters in range(len(message)):
        if ord(message[letters])-97>=0 and ord(message[letters])-97<=26 and message[letters]!="j":
            shortened_message+=message[letters]
    shortened_message=list(shortened_message)
    message=list(message)
    for letters in range(len(shortened_message)-1):
        if shortened_message[letters-count]==shortened_message[letters+1-count]:
            shortened_message.insert(letters+1,"x")
            message.insert(letters+1,"x")
            count+=1
    shortened_message="".join(shortened_message)
    message="".join(message)
    count=0
    if len(shortened_message)%2!=0:
        shortened_message+="x"
        odd=True
    for letters in range(0,len(shortened_message),2):
        letterCode1,letterCode2=0,0 # We get one peer
        for lines1 in grid1:
            for col1 in range(5):
                if shortened_message[letters]==lines1[col1]:
                    letterCode1=[grid1.index(lines1),col1]
        for lines4 in grid4:
            for col4 in range(5):
                if shortened_message[letters+1]==lines4[col4]:
                    letterCode2=[grid4.index(lines4),col4]
        shrt_message_encrypted+=grid2[letterCode1[0]][letterCode2[1]]+grid3[letterCode2[0]][letterCode1[1]]
    for letters in range(len(message)-1):
        if ord(message[letters])-97>=0 and ord(message[letters])-97<=26:
            final_message+=shrt_message_encrypted[letters-count]
        else:
            final_message+=message[letters]
            count+=1
    if odd==True:
        final_message+="x"+message[-1]
    else:
        final_message+=message[-1]
    return final_message
# Main Script
print("----------------------------")
print("------ Code 4-SQUARES ------")
print("----------------------------")
passeword = [input(f"Write the password n°{i+1} please: ") for i in range(4)]
grid1=Grid(passeword[0])
grid2=Grid(passeword[1])
grid3=Grid(passeword[2])
grid4=Grid(passeword[3])
sentence = input("what message do you want to encrypt ?: ")
print("La phrase chiffrée est :")
print(Square(grid1,grid2,grid3,grid4,sentence))