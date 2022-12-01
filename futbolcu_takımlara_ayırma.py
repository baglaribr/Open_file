# Futbolcu takımlara ayırma programı

def futbolcu(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    takım = liste[1]
    return isim + "---" + takım + "\n"

with open("futbolcular.txt","r+",encoding="utf-8") as file:
    fb_listesi = []
    gs_listesi = []
    bjk_listesi = []
    
    for i in file:
        if ("Fenerbahçe" in futbolcu(i)):
            fb_listesi.append(futbolcu(i))
        elif ("Galatasaray" in futbolcu(i)):
            gs_listesi.append(futbolcu(i))
        elif ("Beşiktaş" in futbolcu(i)):
            bjk_listesi.append(futbolcu(i))

    with open("fb.txt","w",encoding="utf-8") as file2:
        for i in fb_listesi:
            file2.write(i)
    
    with open("gs.txt","w",encoding="utf-8") as file3:
        for i in gs_listesi:
            file3.write(i)
    
    with open("bjk.txt","w",encoding="utf-8") as file4:
        for i in bjk_listesi:
            file4.write(i)