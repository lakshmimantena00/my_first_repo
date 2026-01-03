d = {
    "Test1": {
        "Mod1": {
            "entry": "0x02 53 23",
            "exit": "0x02 59 24"
        },
        "Mod2": {
            "entry": "0x03 13 02",
            "exit": "0x03 50 24"
        }
    },
    "Test2": {
        "Mod1": {
            "entry": "0x04 03 23",
            "exit": "0x04 20 24"
        },
        "Mod2": {
            "entry": "0x03 13 02",
            "exit": "0x03 50 24"
        }
    }
}
# print(d["Test1"]["Mod1"]["entry"])
# print(d["Test2"]) 
for x in d.items():
	print(x)