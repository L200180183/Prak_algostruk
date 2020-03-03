def jumlahHurufVokal(text):
    vokal = 'aiueoAIUEO'
    jumlahVokal = ""
    for i in text:
        if i in vokal:
            jumlahVokal += i
    x = [len(text), len(jumlahVokal)]
    return x

def jumlahHurufKonsonan(text):
    konsonan = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    jumlahKonsonan = ""
    for i in text:
        if i in konsonan:
            jumlahKonsonan += i
    x = [len(text), len(jumlahKonsonan)]
    return x
