from etl_ap import etl_ap #Librería desarrollada por Elico
from datetime import datetime
import pytz
import json
import requests
from time import sleep
import snap7
import struct
import csv
from snap7.exceptions import Snap7Exception
from requests.exceptions import RequestException

variables = [
"MotorDosificadorEnergiaConsumidaRefA",
"Motor1rEnergiaConsumidaRefA",
"Motor2rEnergiaConsumidaRefA",
"Motor3rEnergiaConsumidaRefA",
"Motor4rEnergiaConsumidaRefA",
"Motor5rEnergiaConsumidaRefA",
"Motor6rEnergiaConsumidaRefA",
"DosificadorEnergiaConsumidaRefA",
"HorneorEnergiaConsumidaRefA",
"EmpaquerEnergiaConsumidaRefA",
"MotorDosificadorEnergiaConsumidaRefB",
"Motor1rEnergiaConsumidaRefB",
"Motor2rEnergiaConsumidaRefB",
"Motor3rEnergiaConsumidaRefB",
"Motor4rEnergiaConsumidaRefB",
"Motor5rEnergiaConsumidaRefB",
"Motor6rEnergiaConsumidaRefB",
"DosificadorEnergiaConsumidaRefB",
"HorneorEnergiaConsumidaRefB",
"EmpaquerEnergiaConsumidaRefB",
"ConsumoGasRefA",
"ConsumoGasRefB",
"Tiempos",
"TiempoParoTotal",
"TiempoReparacionTotal",
"TiempoArranqueTotal",
"TiempoOperacionEfectivoTotal",
"TiempoEfectivoTotal",
"Produccion",
"UnidadesRechazadasRefA",
"UnidadesAceptadasRefA",
"UnidadesProcesadasRefA",
"UnidadesRechazadasRefB",
"UnidadesAceptadasRefB",
"UnidadesProcesadasRefB",
"UnidadesRechazadasTotales",
"UnidadesAceptadasTotales",
"UnidadesProcesadasTotales",
"ValoresReferencia",
"UnidadesReferenciaRefA",
"UnidadesReferenciaRefB",
"UnidadesReferenciaTotales",
"EnergiaElectricaReferencia",
"GasReferencia",
"TiempoReferencia",
"ValoresEstandar",
"UnidadesEstandar",
"EnergiaElectricaEstandar",
"GasEstandar",
"Fallas",
"FallasTotal",
"FallasReparadasTotal",
"FallasPendientesTotal",
"FallasBits",
"Falla 1",
"Falla 2",


]

etl_ALP = etl_ap.etl_ap(
    ip='192.168.0.10', 
    rack=0, slot=1, name='plc_1', 
    route_log='/home/elicoubuntu/Documents/etl2.log', 
    url_api="",
    token='',
    variables=variables,
    db=1,
)

etl_ALP.run()