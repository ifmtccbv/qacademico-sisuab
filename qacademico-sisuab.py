#! ./env/bin/python
# coding: utf-8

from pathlib import Path
import pandas as pd

home_dir = str(Path.home())

materia = 'matematica'

entrada = pd.read_csv(home_dir+'/Documents/alunos_{}.csv'.format(materia),
                      sep=',', dtype=str, encoding='latin-1')

alunos = []

polos = []

for indice, dados in entrada.iterrows():

    #

    cpf = dados['CPF']

    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    #

    cep = dados['C.E.P.']

    cep = cep.replace('-', '')

    if cep == '        ':
        cep = '00000000'

    #

    cfi = dados['Tipo Forma Ingresso no Período']

    if pd.isna(cfi):
        cfi = 'VE'

    #

    pi = dados['Per. Letivo Inicial']
    pi = pi.split('/')
    pi = int(pi[1])
    pi = '{:02d}'.format(pi)

    #

    cvo = 'DS'

    #

    csi = 'CUR'

    #

    csa = 'CUR'

    #

    email = dados['E-mail']

    #

    telefones = dados['Telefones']

    telefones = telefones.split(', ')

    temp = telefones[0]
    temp = temp.split(' ')

    if len(temp) == 2:
        ddd = '0' + temp[0].replace('(', '').replace(')', '')
        telefone = temp[1].replace('-', '')
    else:
        ddd = '000'
        telefone = '00000000'

    #

    ramal = '0000'

    #

    polo = dados['Pólo Municipal']

    polo = polo.split(' - ')
    polo = int(polo[0])

    #

    aluno = {}

    aluno['polo'] = polo
    aluno['cpf'] = cpf
    aluno['cep'] = cep
    aluno['cfi'] = cfi
    aluno['pi'] = pi
    aluno['cvo'] = cvo
    aluno['csi'] = csi
    aluno['csa'] = csa
    aluno['email'] = email
    aluno['ddd'] = ddd
    aluno['telefone'] = telefone
    aluno['ramal'] = ramal

    alunos.append(aluno)

    #

    if not polo in polos:
        polos.append(polo)

for polo in polos:

    lista = []

    for aluno in alunos:

        if aluno['polo'] == polo:

            lista.append(aluno)

    saida = pd.DataFrame(lista, columns=['cpf', 'cep', 'cfi', 'pi', 'cvo',
                                         'csi', 'csa', 'email', 'ddd', 'telefone', 'ramal'])

    saida.to_csv(home_dir+'/Downloads/Sisuab-{}-{:03d}.csv'.format(materia, polo),
                 sep=';', header=False, index=False, encoding='utf-8')
