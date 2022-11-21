import muveletek
for i in range(4):

    szam1=int(input('Kérem az első számot! '))
    szam2=int(input('Kérem a második számot! '))
    muvelet=input('Milyen műveletet végezzek el (+ / - *)? ')
    if muvelet == '+':
        print(f'{szam1} {muvelet} {szam2} = {muveletek.osszead(szam1, szam2)}')
    elif muvelet == '-':
        print(f'{szam1} {muvelet} {szam2} = {muveletek.kivon(szam1, szam2)}')
    elif muvelet == '/':
        print(f'{szam1} {muvelet} {szam2} = {muveletek.oszt(szam1, szam2)}')
    elif muvelet == '*':
        print(f'{szam1} {muvelet} {szam2} = {muveletek.szoroz(szam1, szam2)}')