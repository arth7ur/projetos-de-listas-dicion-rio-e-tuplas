estado= dict()
brasil= list()
for c in range(0, 3):
    estado['uf'] =str(input('UNIDADE FEDERATIVA:'))
    estado['sigla']=str(input('SIGRA do ESTADO:'))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'o campo {k} tem valor {v}') 
