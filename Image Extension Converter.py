from PIL import Image
from PySimpleGUI import Text,Button,Combo,Button,theme,Window,Input,FileBrowse,FolderBrowse

# JPG PNG JPEG BMP
def success(path):
    theme("DarkTeal7")
    lyt=[[Text("\t")]+[Text("Converted Successfully and Saved as ",font=("Helvetica",15))]+[Text("\t")],
         [Text(path)],
                 [Button("OK",button_color="green2",size=(10,1))]]
    wnd=Window("Success",lyt,element_justification="c",keep_on_top=True)
    event,values=wnd.read()
    wnd.close()
    mn()
def fail(s):
    theme("DarkTeal7")
    lyt=[[Text("\t")]+[Text("Task Failed due to an Unknwn Error",font=("Helvetica",15))]+[Text("\t")],
         [Text(s)],
                 [Button("OK",button_color="red",size=(10,1))]]
    wnd=Window("Failed",lyt,element_justification="c",keep_on_top=True)
    event,values=wnd.read()
    wnd.close()
    mn()
def alert(tx):
    theme("Topanga")
    lyt=[[Text("\t")]+[Text(tx,font=("Helvetica",15))]+[Text("\t")],
                 [Button("OK",button_color="red",size=(10,1))]]
    wnd=Window("Alert !!!",lyt,element_justification="c",keep_on_top=True)
    event,values=wnd.read()
    wnd.close()
def alert_y_n(tx):
    theme("Topanga")
    lyt=[[Text("\t")]+[Text(tx,font=("Helvetica",15))]+[Text("\t")],
                 [Button("Yes",button_color=("green2","black"),size=(10,1))]+
         [Button("No",button_color=("red","black"),size=(10,1))]]
    wnd=Window(" ",lyt,element_justification="c",keep_on_top=True)
    event,values=wnd.read()
    wnd.close()
    return event
def convert2(e,s,p,dk):
    if e=="PNG":
        l=["JPG","JPEG","BMP"]
    elif e=="JPG":
        l=["PNG","JPEG","BMP"]
    elif e=="JPEG":
        l=["PNG","JPG","BMP"]
    elif l=="BMP":
        l=["PNG","JPG","JPEG"]
    theme("DarkTeal7")
    lt=[[Text()],[Text("Convert From : "+e,font=("Chilanka",20),key="-C1-" )],[Text("Convert to : ",font=("Chilanka",20))]+
        [Combo(l,default_value=l[0],key="board")],[Text()],
        [Button("Convert >>",size=(10,1))]+[Button("Abort",size=(10,1))]]
    window=Window("Converter",lt,element_justification="c",size=(400,200))
    event,v=window.read()
    if event=="Abort" or event==None:
        window.close()
        convert()
    window.close()
    if v["board"] in ["JPG","PNG","JPEG","BMP"]:
        try:
            im = Image.open(s)
            pt=p+"/"+dk+"."+v["board"].lower()
            im.save(pt)
            success(pt)
        except:
            fail(s)
    else:
        convert2(e,s,p,dk)
def convert():
    theme("DarkTeal7")
    lt=[[Text("Select Image",font=("Chilanka",20))],[Input()]+[FileBrowse()],
        [Text()],[Text("Select Output Folder",font=("Chilanka",20))],[Input()]+[FolderBrowse()],[Text()],
        [Button("Next >>",size=(10,1))]+[Button("Abort",size=(10,1))]]
    wn=Window("Converter",lt)
    e,v=wn.read()
    if e==None or e=="Abort":
        wn.close()
        mn()
    f=v["Browse"]
    f=f.split("/")
    f=f[-1]
    f=f.split(".")
    dk=f[0]
    dt=f[-1]
    img_ext=dt.upper()
    if v["Browse"]!="":
        if v["Browse0"]!="":
            if img_ext in ["PNG","JPG","JPEG","BMP"]:
                wn.close()
                convert2(img_ext,v["Browse"],v["Browse0"],dk)
            else:
                alert("You Can Only Use PNG,JPG,JPEG and BMP Images Only")
                wn.close()
                convert()
        else:
            wn.close()
            convert()
    else:
        wn.close()
        convert()
def about():
    theme("DarkTeal7")
    lt=[[Text("## ABOUT ##",font=("Helvetica",20))],
            [Text("---------------------------",font=("Helvetica",20))],
            [Text("* A PR@16 Creation\n* Using this tool, you can convert Image extension\n* @@ Steps @@\n* 1. Select output folder to where converted Image\n      should be saved\n* 2. .png ,.jpg ,.jpeg and .bmp image formats are supported\n* 3. Select your Extension and Continue\n* 4. It will be Saved at the destination folder with same\n      file name as souce file\n* Compiled and Created by PR@16 Creations\n* Credits: PR@16 Creations",font=("Helvetica",15))],
            [Text("---------------------------",font=("Helvetica",20))],
            [Button("OK",size=(80,2),button_color=("black","lightblue"))]]
    wn=Window("Help",lt)
    e,v=wn.read()
    wn.close()
    mn()
def mn():
    theme("DarkTeal7")
    layout1=[[Text("\nImage Format",font=("Chilanka",25))],[Text("Converter\n",font=("Chilanka",25))],[Button("Convert",font=("Helvetica",20),button_color=("black","green2"),size=(100,1),bind_return_key=True)],
                             [Button("About",font=("Helvetica",20),size=(100,1),button_color=("black","yellow"),bind_return_key=True)],
                             [Button("Exit",font=("Helvetica",20),size=(100,1),button_color=("black","red"),bind_return_key=True)],[Text()],
                             [Text("\nVersion 2.1.8",font=("Chilanka"))]]
    window1=Window("Image Format Converter",layout1,size=(390, 400),element_justification="c")
    event,values=window1.read()
    if event=="Convert":
        window1.close()
        convert()
    elif event=="About":
        window1.close()
        about()
    else:
        window1.close()
        exit()
mn()
