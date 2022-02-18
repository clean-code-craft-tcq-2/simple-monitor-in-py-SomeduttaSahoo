
def PrintoutofRange(parameter,value):
  print(parameter ,'with the reading',value,'is out of the range!')
  
  
def isTemperatureInRange(temperature):
  temperatur=convertTocelsius(temperature)
  if temperature < 0 :
    return False
  elif temperature > 45 :
    return False
  else:
    return True
  
def issocInRange(soc):
  if soc < 20 :
    return False
  elif soc > 80 :
    return False
  else:
    return True
  
def ischarge_rateInRange(charge_rate):
  if charge_rate > 0.8:
    return False
  else:
    return True
 
def convertTocelsius(temperature):
  if('f' in temperature.lower() ):
    return((int(temperature.lower().split('f')[0])-32.0)*(5.0/9.0))
  elif('k' in temperature.lower()):
    return(int(temperature.lower().split('k')[0])-273.0)
  else:
    return(int(temperature.lower().split('c')[0]))

  
def battery_is_ok(temperature, soc, charge_rate):
Checktemperature=isTemperatureInRange(temperature)
Checksoc=issocInRange(soc)
Checkcharge_rate=ischarge_rateInRange(charge_rate)
  
return Checktemperature and Checksoc and Checkcharge_rate


if __name__ == '__main__':
  assert(battery_is_ok("25c", 70, 0.7) is True)
  assert(battery_is_ok("50c", 85, 0) is False)
  assert(battery_is_ok("100f", 85, 0) is False)
  assert(battery_is_ok("271k", 85, 0) is False)
