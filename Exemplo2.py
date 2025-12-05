previsoes=['Ensolarado','Nublado','Chuvoso','Tempestade','Ensolarado']
print(previsoes)

PREVISAO_FELIZ='Ensolarado'

for p in previsoes:
    print(p)

    if p==PREVISAO_FELIZ:
        print('Aproveite para passear')
    else:
        print('Não saia de casa sem o guarda chuva')    