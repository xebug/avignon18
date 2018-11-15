import datetime

def getID():
    n = input('Entrez votre nom : ')
    p = input ('Entrez votre prenom : ')
    t = datetime.datetime.now()
    s = n + p + t.strftime('%Y/%m/%d,%H:%M:%S')
    j = len(s)
    h = 0
    i = 0
    
    while j < 32:
            s = s + "0"
            j = j + 1 

    while i < 32:  
        h = 31 * h + ord(s[i])
        i = i + 1
    
    return h

print(getID())

