import tkinter
import time
from urllib import request
import datetime
root = tkinter.Tk()
root.title("配信チェッカー")
root.geometry("700x600")

def main(name,url):
    res=request.urlopen(url)
    content=res.read()
    html=content.decode()
    test="startTime\":\""
    idx=html.find(test)
    live=html.find("人が視聴中")
    name1=tkinter.Label(text=name,background="#ffff00",width=70,height=1)
    name1.pack()
    if idx==-1 and live==-1:
        nasi=tkinter.Label(text="枠なし",background='#ff7f00',width=10)
        nasi.pack()
        #print("枠なし")
        kuhaku()
    elif live!=-1:
        livenow=tkinter.Label(text="配信中",fg="white",background='#ff0000',width=10)
        livenow.pack()
        #print("配信中")
        kuhaku()
    else:
        r=html[idx+len(test):idx+len(test)+10]
        html2=html[idx+len(test)+10:]
        idx2=html2.find(test)
        startTime=datetime.datetime.fromtimestamp(int(r))
        timesub=startTime-datetime.datetime.fromtimestamp(int(time.time()))
        ari1=tkinter.Label(text="直近："+str(startTime)+"\t\tあと "+str(timesub),background='#33ffff')
        ari1.pack()
        #print("直近："+str(datetime.datetime.fromtimestamp(int(r))))
        r2=html2[idx2+len(test):idx2+len(test)+10]
        if idx2!=-1 and r2!=r:#r2!=r:#今後のライブストリームに違うものが表示された場合
            ari2=tkinter.Label(text="その次："+str(datetime.datetime.fromtimestamp(int(r2))),background='#33ffff')
            ari2.pack()
            #print("その次："+str(datetime.datetime.fromtimestamp(int(r2))))
            kuhaku()
        else:
            kuhaku()

def kuhaku():
    ku=tkinter.Label()
    ku.pack()

channel=[["Miko Ch. さくらみこ","https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA"],
["Okayu Ch. 猫又おかゆ","https://www.youtube.com/channel/UCvaTdHTWBGv3MKj3KVqJVCw"],
["Nene Ch.桃鈴ねね","https://www.youtube.com/channel/UCAWSyEs_Io8MtpY3m-zqILA"],
["Subaru Ch. 大空スバル","https://www.youtube.com/channel/UCvzGlP9oQwU--Y0r9id_jnA"],
["Marine Ch. 宝鐘マリン ","https://www.youtube.com/channel/UCCzUftO8KOVkV4wQG1vkUvg"],
["Polka Ch. 尾丸ポルカ","https://www.youtube.com/channel/UCK9V2B22uJYu3N7eR_BT9QA"],
["Tamaki Ch. 犬山たまき / 佃煮のりお","https://www.youtube.com/channel/UC8NZiqKx6fsDT3AVcMiVFyA"],
["星川サラ / Sara Hoshikawa","https://www.youtube.com/channel/UC9V3Y3_uzU5e-usObb6IE1w"]]
a=0
while a<len(channel):
    main(channel[a][0],channel[a][1])
    print("読み込み中："+str((a+1)/len(channel)*100)+"%")
    a+=1
root.mainloop()