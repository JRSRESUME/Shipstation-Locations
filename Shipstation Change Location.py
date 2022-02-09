from urllib.request import Request, urlopen
import json
import os 


k = 5
while 5> 0:
  sku = input("Enter Sku ")

  if sku == "q":
    quit()
  headers = {
  'Authorization': 'Enter your authorization key here',
  'Content-Type': 'application/json'
  }

  request = Request('https://ssapi.shipstation.com/products?sku='+sku, headers=headers)
  response_body = urlopen(request)
  data = json.load(response_body)

  theids = []
  thelocs = []

  for item in data ['products']:
    theids.append(item ['productId'])
    thelocs.append(item ['warehouseLocation'])

  print("Location")
  try:
    print(thelocs[0])
  except IndexError:
    print("Sku Does Not Exist")
  

  newloc = input("Enter New Location ")


  for poop in theids:
    values = {
    "aliases": None,
    "productId": poop,
    "sku": "",
    "name": "",
    "price": 0,
    "defaultCost": None,
    "length": None,
    "width": None,
    "height": None,
    "weightOz": None,
    "internalNotes": None,
    "fulfillmentSku": None,
    "active": True,
    "productCategory": None,
    "productType": None,
    "warehouseLocation": newloc,
    "defaultCarrierCode": None,
    "defaultServiceCode": None,
    "defaultPackageCode": None,
    "defaultIntlCarrierCode": None,
    "defaultIntlServiceCode": None,
    "defaultIntlPackageCode": None,
    "defaultConfirmation": None,
    "defaultIntlConfirmation": None,
    "customsDescription": None,
    "customsValue": None,
    "customsTariffNo": None,
    "customsCountryCode": None,
    "noCustoms": None,
    "tags": None
    }
    request = Request('https://ssapi.shipstation.com/products/'+str(poop),headers=headers, data=bytes(json.dumps(values), encoding="utf-8",))
    request.get_method = lambda: 'PUT'
    response_body = urlopen(request)
    os.system('cls')