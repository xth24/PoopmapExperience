import poopmap

poop = poopmap.Poopmap()

print(f"""
poop device data:
{poop.device_id}
{poop.token}
""")

result = poop.drop_a_poop(
    longitude=1,
    latitude=1
)

print(result)