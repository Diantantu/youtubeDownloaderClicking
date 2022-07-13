from os import link
from platform import python_branch
import time
import pyautogui




links = ["https://www.youtube.com/watch?v=-F-knMQzgWU&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=1",
"https://www.youtube.com/watch?v=4EIO6Ma0foA&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=2",
"https://www.youtube.com/watch?v=wEk0oBzGC6M&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=3",
"https://www.youtube.com/watch?v=Zj04S_UOYzw&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=4",
"https://www.youtube.com/watch?v=i3vWPr0xvDU&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=5",
"https://www.youtube.com/watch?v=cOZDezhef3o&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=6",
"https://www.youtube.com/watch?v=uP9DdcipNvg&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=7",
"https://www.youtube.com/watch?v=hNlAzBushZ0&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=8",
"https://www.youtube.com/watch?v=WfvVUL-WQVs&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=9",
"https://www.youtube.com/watch?v=giOOtn4AQxE&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=10",
"https://www.youtube.com/watch?v=NbqqlAwChOQ&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=11",
"https://www.youtube.com/watch?v=vC6fIQAX1N8&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=12",
"https://www.youtube.com/watch?v=MTH9bEkBm9w&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=13",
"https://www.youtube.com/watch?v=_YVXarhu-io&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=14",
"https://www.youtube.com/watch?v=4meY7WSk2-Y&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=15",
"https://www.youtube.com/watch?v=qE76uyWSLR8&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=16",
"https://www.youtube.com/watch?v=krHwI-nlloM&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=17",
"https://www.youtube.com/watch?v=_aoi9GurBNE&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=18",
"https://www.youtube.com/watch?v=q6AblFEplEQ&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=19",
"https://www.youtube.com/watch?v=X1f7bHZTSGs&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=20",
"https://www.youtube.com/watch?v=zlFcWwAOY54&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=21",
"https://www.youtube.com/watch?v=jxWzbjhihtg&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=22",
"https://www.youtube.com/watch?v=-qExeM_Xk3s&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=23",
"https://www.youtube.com/watch?v=obRpiRL2Fns&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=24",
"https://www.youtube.com/watch?v=qA4Rl8sPKAk&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=25",
"https://www.youtube.com/watch?v=JjKn7deNcvU&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=26",
"https://www.youtube.com/watch?v=VqjnM85f-z4&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=27",
"https://www.youtube.com/watch?v=i2DRjhiHewA&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=28",
"https://www.youtube.com/watch?v=V7sk4ttVzkk&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=29",
"https://www.youtube.com/watch?v=vb4ZZwBBlCk&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=30",
"https://www.youtube.com/watch?v=xTmZIDfrQVE&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=31",
"https://www.youtube.com/watch?v=2B_skmB_Ucs&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=32",
"https://www.youtube.com/watch?v=SA4d8nd5rxM&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=33",
"https://www.youtube.com/watch?v=qUU_JNBbN7A&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=34",
"https://www.youtube.com/watch?v=usoZfyFhcGw&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=35",
"https://www.youtube.com/watch?v=L-c6c3cLQSA&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=36",
"https://www.youtube.com/watch?v=gwgLz6P7a24&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=37",
"https://www.youtube.com/watch?v=NZ3yW7h9Xjw&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=38",
"https://www.youtube.com/watch?v=HuAGMPQlTZ4&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=39",
"https://www.youtube.com/watch?v=7_ipamH2ok4&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=40",
"https://www.youtube.com/watch?v=85Y2TdjpNRE&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=41",
"https://www.youtube.com/watch?v=Idbmi03D7Hs&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=42",
"https://www.youtube.com/watch?v=vFBiRRc5TLw&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=43",
"https://www.youtube.com/watch?v=gslS_zNLnuk&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=44",
"https://www.youtube.com/watch?v=y4veNnLzDE8&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=45",
"https://www.youtube.com/watch?v=yiaIp41yYVc&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=46",
"https://www.youtube.com/watch?v=_FkKHay7FrY&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=47",
"https://www.youtube.com/watch?v=cOjLiZzGSqs&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=48",
"https://www.youtube.com/watch?v=QADVQM6oo1g&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=49",
"https://www.youtube.com/watch?v=tl1aNCnkd9M&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=50",
"https://www.youtube.com/watch?v=pon1ltGvzY4&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=51",
"https://www.youtube.com/watch?v=9qDjzcKO6XU&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=52",
"https://www.youtube.com/watch?v=vSAx2JzHtVI&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=53",
"https://www.youtube.com/watch?v=ezRkSY5UJQI&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=54",
"https://www.youtube.com/watch?v=JLHSaBC8UHk&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=55",
"https://www.youtube.com/watch?v=uPs8WYYczI8&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=56",
"https://www.youtube.com/watch?v=W2-n9o463Qc&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=57",
"https://www.youtube.com/watch?v=CKERhz3VjSw&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=58",
"https://www.youtube.com/watch?v=atQTXHXu5Uc&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=59",
"https://www.youtube.com/watch?v=AXyBAIrfuO8&list=PLozhsZB1lLUMWiSiVrcihCtfG1WptrRN5&index=60"]

for x in links:
    pyautogui.moveTo(710, 795, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(1204, 407, duration = 1)
    pyautogui.click()
    pyautogui.scroll(1000)
    pyautogui.moveTo(792, 273, duration = 1)
    pyautogui.click()
    pyautogui.typewrite(x)
    pyautogui.moveTo(831, 267, duration = 1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(831, 267, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(666, 550, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(710, 795, duration = 1)
    pyautogui.click()
    time.sleep(5)
