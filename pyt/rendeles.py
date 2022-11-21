nyit=8
zar=12
jelenido=int(input('Hány óra van most? '))
if nyit <= jelenido < zar:
    print('Ennyi perced van még odaérni:', (zar-jelenido)*60)
else:  # jelenido < nyit or jelenido >= zar
    if jelenido < nyit:
        ido_nyitasig = nyit - jelenido
        print('Még nem rendel a doktorúr, sürgős esetben hívja az ügyeletet, vagy ennyi idő múlva keresse a rendelőben:', ido_nyitasig*60)
    else:
        print('Ma már nem rendel a doktorúr, keresse holnap reggel, sürgős esetben hívja az ügyeletet!')