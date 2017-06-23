#!/usr/bin/env python

import json

print 'Prebacivanje kolona'

f_back = open('backup.csv','r')

f_pre = open('backup_preimenovano.csv','w')
f_mapa = open('mapa_preimenovanih.json','w')

prva_linija = f_back.readline()
svi_podaci = []

cetvrto_niz = []
peto_niz = []
osmo_niz = []
deveto_niz = []

for linija in f_back:
	linija_niz = linija.split(',')
	svi_podaci.append(linija_niz)
	cetvrto_niz.append(linija_niz[4])
	peto_niz.append(linija_niz[5])
	osmo_niz.append(linija_niz[8])
	deveto_niz.append(linija_niz[9])
	
cetvrto_skup = set(cetvrto_niz)
peto_skup = set(peto_niz)
osmo_skup = set(osmo_niz)
deveto_skup = set(deveto_niz)

cetvrto_duzina = range(1,len(list(cetvrto_skup))+1)
peto_duzina = range(1,len(list(peto_skup))+1)
osmo_duzina = range(1,len(list(osmo_skup))+1)
deveto_duzina = range(1,len(list(deveto_skup))+1)

cetvrto_mapa = dict(zip(cetvrto_skup,cetvrto_duzina))
peto_mapa = dict(zip(peto_skup,peto_duzina))
osmo_mapa = dict(zip(osmo_skup,osmo_duzina))
deveto_mapa = dict(zip(deveto_skup,deveto_duzina))

json.dump([cetvrto_mapa, peto_mapa, osmo_mapa, deveto_mapa], f_mapa)

for podatak in svi_podaci:
	podatak[4] = str(cetvrto_mapa[podatak[4]])
	podatak[5] = str(peto_mapa[podatak[5]])
	podatak[8] = str(osmo_mapa[podatak[8]])
	podatak[9] = str(deveto_mapa[podatak[9]])
	f_pre.write(','.join(podatak))
	
