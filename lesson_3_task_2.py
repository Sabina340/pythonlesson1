from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14", "+79991112233"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79992223344"))
catalog.append(Smartphone("Xiaomi", "12 Pro", "+79993334455"))
catalog.append(Smartphone("Google", "Pixel 8", "+79994445566"))
catalog.append(Smartphone("Honor", "Magic 5", "+79995556677"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")