from django.shortcuts import render
from django.http import HttpResponse
from smartcard.System import readers
import json

def readCard(request):
    response_data = {}
    response_error= {}
    # define the APDUs used in this script
    COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]

    # get all the available readers
    r = readers()
    if len(r) > 0:
        reader = r[0]
        try:
            connection = reader.createConnection()
            connection.connect()
            data, sw1, sw2 = connection.transmit(COMMAND)
            response_data['reader'] = str(reader)
            response_data['UUIDec'] = str(data)
            response_data['UUIDHex'] = "".join(['{:02X}'.format(h) for h in data])
            response_data['command'] = str(sw1) + " " + str(sw2)
            response_data['message'] = "Ok"
            #raise Exception('hola')
        except Exception:
            response_error['error'] = 'No se detecto ninguna tarjeta'
            return HttpResponse(json.dumps(response_error), content_type="application/json")
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_error['error'] = 'No se detecto ningun lector'
        return HttpResponse(json.dumps(response_error), content_type="application/json")
