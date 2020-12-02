import json
import requests
import os
import datetime
import urllib
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr
from users import users
from boto3.dynamodb.conditions import Key
from bs4 import BeautifulSoup
import logging
from decimal import Decimal


TELE_TOKEN=os.getenv('TELEGRAM_TOKEN')
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)
# keyboard = [["/adi"],["/brai"],["/facu"],["/jali"],["/luqui"],["/nan"],["/niki"],["/zeki"]]

def lambda_handler(event, context):
    
    message = json.loads(event['body'])
        
    try:

        chat_id = message['message']['chat']['id']
        first_name = message['message']['from']['first_name']
        id = message['message']['from']['id']
        reply = message['message']['text']
        user = users.get(id,"error de usuario, quien sos?")
        
        if '/hola' in reply:
            rta = "Hola {}!".format(user)
            send_message(rta,chat_id)
        elif '/debug' in reply:
            rta = str(message)
            send_message(rta,chat_id)
        # elif '/event' in reply:
        #     rta = str(event)
        #     send_message(rta,chat_id)    
        elif '/disclaimer' in reply:
            rta = "Las posiciones expresadas por mí son solo mías y no contemplan ninguna obligación del/hacia el ritual ni imposición a ningún otro hermano. Háganse coger"
            send_message(rta, chat_id)
        elif '/jalio' in reply:
            futuredate = datetime.strptime('Sep 30 2021  22:15', '%b %d %Y %H:%M')
            nowdate = datetime.now()
            count = int((futuredate-nowdate).total_seconds())
            days = count//86400
            hours = (count-days*86400)//3600
            minutes = (count-days*86400-hours*3600)//60
            seconds = count-days*86400-hours*3600-minutes*60
            rta = "{} dias, {} horas, {} minutos, {} segundos para que Jalio vuelva a tomar en vaso de vidrio".format(days, hours, minutes, seconds)
            send_message(rta,chat_id)
        elif '/puntos' in reply:
            #keyboard = build_keyboard()
            rta = "Elegi a quien darle tus puntos de Gryffindor!!!"+"\n"+"pone / seguido del nombre del hermano"  \
            + "\n" + "(nombres validos: adi, brai, facu, jali, luqui, nan, niki, zeki)"
            #send_message("Elegi a quien darle tus puntos de Gryffindor!!!",chat_id, keyboard)
            send_message(rta,chat_id)
            
        elif '/supermatch' in reply:
            dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
            table = dynamodb.Table('puntos_asado')
            response = table.scan()
            data = response['Items']
            while 'LastEvaluatedKey' in response:
	            response = table.scan(ExclusiveStartKey = response['LastEvaluatedKey'])
	            data.extend(response['Items'])
            data_linda = str()
            for mi_json in data:
                data_linda += mi_json["hermano"] + ": " + str(mi_json["puntos"]) + "\n" 
            rta = "Tabla de puntos" + "\n" + "\n" + str(data_linda)
            send_message(rta,chat_id)
            

        elif "/adi" in reply:
            if user == "adi":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"adi",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
        
            
        elif "/brai" in reply:
            if user == "brai":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"brai",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
            
        elif "/facu" in reply:
            if user == "facu":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"facu",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
        
        elif "/jali" in reply:
            if user == "jali":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"jali",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
            
        elif "/luqui" in reply:
            if user == "luqui":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"luqui",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
            
        elif "/nan" in reply:
            if user == "nan":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"nan",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
            
        elif "/niki" in reply:
            if user == "niki":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"niki",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
            
        elif "/zeki" in reply:
            if user == "zeki":
                rta = "No podes darte puntos a vos, no seas trucho"
            else:
                try:
                    cant = float(reply.split(" ")[-1])
                    cant = Decimal(str(cant))
                    rta = sumar_puntos(user,"zeki",cant)
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma)"
        
            send_message(rta,chat_id)
            
        elif "/cuenta" in reply:
            dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
            table = dynamodb.Table('cuenta_asado')
            response = table.scan()
            data = response['Items']
            while 'LastEvaluatedKey' in response:
	            response = table.scan(ExclusiveStartKey = response['LastEvaluatedKey'])
	            data.extend(response['Items'])
            data_linda = str()
            for mi_json in data:
                data_linda += mi_json["moneda"] + ": $ " + str(mi_json["cantidad"]) + "\n" 
            rta = "Estado de cuenta"+ "\n" + "\n" + str(data_linda)
            send_message(rta,chat_id)

            
        elif "/pesos" in reply:
            if user == "adi": 
                try:
                    cant = float(reply.split(" ")[-1]) #tomo el valor del comando "/dolares 500"
                    cant = Decimal(str(cant)) #convierto a Decimal porque boto3 no me acepta float, pero el Exception lo tengo hecho con ValueError...
                    dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
                    table = dynamodb.Table('cuenta_asado')
                
                    response = table.update_item(
                        Key={
                            'moneda': 'pesos'
                        },
                        UpdateExpression = "SET cantidad = :var",
                        ExpressionAttributeValues = {
                            ":var": cant
                        },
                        ReturnValues = "UPDATED_NEW"
                    )
                    rta = "Actualizado!"
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma). El formato es (por ej) /dolares 500"
                
                send_message(rta,chat_id)
                
            else:
                rta = "No estas autorizado a cambiar el estado de cuenta!"
                send_message(rta,chat_id)  
        
        elif "/dolares" in reply:
            if user == "adi":
                try:
                    cant = float(reply.split(" ")[-1]) #tomo el valor del comando "/dolares 500"
                    cant = Decimal(str(cant)) #convierto a Decimal porque boto3 no me acepta float, pero el Exception lo tengo hecho con ValueError...
                    dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
                    table = dynamodb.Table('cuenta_asado')
                
                    response = table.update_item(
                        Key={
                            'moneda': 'dolares'
                        },
                        UpdateExpression = "SET cantidad = :var",
                        ExpressionAttributeValues = {
                            ":var": cant
                        },
                        ReturnValues = "UPDATED_NEW"
                    )
                    rta = "Actualizado!"
                except ValueError as e:
                    logging.error('Error at %s', 'division', exc_info=e)
                    rta = "Error: solo son validos numeros (punto en lugar de coma). El formato es (por ej) /dolares 500"
                
                send_message(rta,chat_id)
                
            else:
                rta = "No estas autorizado a cambiar el estado de cuenta!"
                send_message(rta,chat_id)    
                
            
        elif "/help" in reply:
            rta = "/hola - te saluda \
            /disclaimer - te tira el disclaimer \
            /jalio - te dice cuanto le falta a Jali para el vidrio \
            /puntos - Elegi a quien darle los puntos de Gryffindor!!! \
            /supermatch - Tabla de puntajes del MVP del asado \
            /cuenta - Estado de cuenta del asado \
            /pesos - Modificar cuenta pesos (usar formato /pesos XXX) (solo gerente) \
            /dolares - Modificar cuenta dolares (usar formato /dolares XXX) (solo gerente) \
            /mispuntos - Te dice cuantos puntos para dar te quedan \
            /elma - te dice que tenes mal humor \
            /asadocoto - te dice el precio de hoy del asado de coto \
            /coto - te dice el precio de varios cortes de coto \
            /dolarblue - Te dice el valor del dolar blue venta en La Nacion a tiempo real"
            
            
            send_message(rta,chat_id)
            
        elif "/elma" in reply:
            rta = "uuuuuuuuhhh el mal humor que tenes!"
            send_message(rta,chat_id)

        elif "/mispuntos" in reply:
            dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
            puntos = dynamodb.Table('puntos_disponibles')
            response_puntos = puntos.query(
                KeyConditionExpression=Key('hermano').eq(user)
            )
            restantes = response_puntos['Items'][0]['cantidad']
            rta = "Tenes {} puntos restantes!".format(restantes)
            send_message(rta,chat_id)
            
        elif "/asadocoto" in reply:
            dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
            precios = dynamodb.Table('precios')
            response = precios.query(
                KeyConditionExpression=Key('corte').eq("asado")
            )
            precio_asado = response['Items'][0]['precio']
            rta = "El asado de tira especial Coto hoy esta {}".format(precio_asado)
            send_message(rta,chat_id)
        
        elif "/coto" in reply:
            dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
            table = dynamodb.Table('precios')
            response = table.scan()
            data = response['Items']
            while 'LastEvaluatedKey' in response:
	            response = table.scan(ExclusiveStartKey = response['LastEvaluatedKey'])
	            data.extend(response['Items'])
            data_linda = str()
            for mi_json in data:
                data_linda += mi_json["corte"] + ": " + str(mi_json["precio"]) + "\n" 
            rta = "Tabla de precios COTO" + "\n" + "\n" + str(data_linda)
            send_message(rta,chat_id)
            
        elif '/dolarblue' in reply:
            try:
                url = "https://www.cronista.com/MercadosOnline/dolar.html"
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                precio_venta = soup.find_all('div', {'class' : 'numDolar'})[3].get_text() #fijarse la página, el valor del dolar venta es el 4to que aparece bajola clase numDolar
                precio_compra = soup.find_all('div', {'class' : 'numDolar'})[2].get_text() #fijarse la página, el valor del dolar venta es el 4to que aparece bajola clase numDolar
                rta = "Precio dolar blue actual (compra / venta) - El Cronista: " + precio_compra + " / " + precio_venta
                send_message(rta,chat_id)
            except Exception as e:
                logging.error('Error at %s', 'division', exc_info=e)
                rta = "Error: no se encuentra valor en la página www.cronista.com/MercadosOnline/dolar.html"
                send_message(rta,chat_id)
            
        return {
            'statusCode': 200,
            'body': str()
        }
    
    except KeyError:
        return {
            'statusCode': 200,
            'body': "KeyError"
    }

    
def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    requests.get(url)


def sumar_puntos(quien,a_quien,cuantos):
    
    if cuantos <= 0:
        
        rta = "no podes restar puntos ni dar 0 puntos"
        return rta
    
    else:
        
        dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
        
        puntos = dynamodb.Table('puntos_disponibles')
        response_puntos = puntos.query(
            KeyConditionExpression=Key('hermano').eq(quien)
        )
        puntos_restantes = response_puntos['Items'][0]['cantidad']
        
        resto = puntos_restantes
        
        if puntos_restantes <= cuantos:
            rta = "No tenes suficientes puntos {}! solamente te quedan {}!".format(quien, resto)
            return rta
        else:    
            puntos.update_item(
                Key={
                    'hermano': quien
                },
                UpdateExpression = "SET cantidad = cantidad - :incr",
                ExpressionAttributeValues = {
                    ":incr": cuantos
                },
                ReturnValues = "UPDATED_NEW"
            )
            table = dynamodb.Table('puntos_asado')
            table.update_item(
                Key={
                    'hermano': a_quien
                },
                UpdateExpression = "SET puntos = puntos + :incr",
                ExpressionAttributeValues = {
                    ":incr": cuantos
                },
                ReturnValues = "UPDATED_NEW"
            )
            rta = "Actualizado!"
            return rta


"""
Listado de comandos:

hola - Te saluda
disclaimer - Te tira el disclaimer
jalio - Te dice cuanto le falta a Jali para el vidrio
puntos - Elegi a quien darle los puntos de Gryffindor!!!
supermatch - Tabla de puntajes del MVP del asado
cuenta - Estado de cuenta del asado
pesos - Modificar cuenta pesos (/pesos -XXX) (solo gerente)
dolares - Modificar cuenta dolares (/dolares -XXX) (solo gerente)
elma - Te dice que tenes mal humor
mispuntos - Te dice cuantos puntos te quedan
asadocoto - te dice el precio del asado de coto
coto - te dice los precios de varios cortes de coto
help - Te dice el listado de comandos
dolarblue - Te dice el valor del dolar blue (venta)

"""