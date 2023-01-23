from datetime import datetime
ahora=datetime.now()
navidad = datetime(2023,12,25)
tiempo_falta = navidad - ahora
print(f"Los dias que faltan son {tiempo_falta.days}")
