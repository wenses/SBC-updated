import kivy, spacy, time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
import os, random
from matplotlib import pyplot as plt
import pandas as pd 
from rank_bm25 import BM25Okapi 
from tqdm import tqdm

Window.clearcolor=(0,200/255.0,0,1)

class Main(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(Label(text='SBC',font_size=49))


        self.add_widget(Label(text='Systematic Business Container',font_size=30))
        self.add_widget(Label())

        self.login=Button(text='LOGIN',background_color=(0,200/255.0,200/255.0,1),font_family='Times New Roman')
        self.add_widget(self.login)
        self.login.bind(on_press=self.go_to_login)

        self.signup=Button(text='SIGNUP',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.signup)
        self.signup.bind(on_press=self.go_to_signup)

    def go_to_login(self,instance):
        sbc.screen_manager.current='login'

    def go_to_signup(self,instance):
        sbc.screen_manager.current='signup'

class Login(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2



        self.add_widget(Label())
        self.add_widget(Label(text='LOGIN',font_size=28))

        self.add_widget(Label(text='Username:',font_size=18))

        self.username=TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:',font_size=18))
        self.password=TextInput(multiline=False,password=True)
        self.add_widget(self.password)

        self.back=Button(text='GO BACK',background_color=(0,200/255.0,200/255.0,1),color=(0,1,0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.go_back)



        self.loging=Button(text='LOGIN',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.loging)
        self.loging.bind(on_press=self.logging_in)

    def go_back(self,instance):
        sbc.screen_manager.current='main'

    def logging_in(self,instance):
        global username
        username=self.username.text
        password=self.password.text
        username=str(username)
        password=str(password)

       # username2=sign_up.go_next.username1
        #password2=sign_up.go_next.password1


        if username=='the wenses media' and password=='business' or password=='password':
            sbc.home.update_info(username)
            sbc.screen_manager.current='home'
        elif username=='mwanyuma' and password=='password':
            sbc.home.update_info(username)
            sbc.screen_manager.current='home'
        elif username=='chizenga' and password=='password':
            sbc.home.update_info(username)
            sbc.screen_manager.current='home'
        elif username=='peter ndaki' and password=='password':
            sbc.home.update_info(username)
            sbc.screen_manager.current='home'
        else:
            sbc.screen_manager.current='error'
            Window.clearcolor=(1,0,0,1)


global username
class Error(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1



        self.add_widget(Label(text='It seems  that you dont have an account to login',font_size=20))
        self.add_widget(Label(text='Try to make an account by signing up below',font_size=20))
        self.add_widget(Label(text='Or you not filled in your login or sign up requirements well',font_size=20))

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.signup=Button(text='SIGN UP',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.signup)
        self.signup.bind(on_press=self.do_signup)

        self.back=Button(text='GO BACK TO START PAGE',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.go_back)

    def go_back(self,instance):
        sbc.screen_manager.current='main'
        Window.clearcolor=(0,200/255.0,0,1)

    def do_signup(self,instance):
        sbc.screen_manager.current='signup'
        Window.clearcolor=(0,200/255.0,0,1)


class Home(GridLayout):
    def __init__(self,**kwargs):
        global username
        super().__init__(**kwargs)
        self.cols=3

        self.add_widget(Label())
        self.add_widget(Label(text='SBC',font_size=35))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label(text='HOME',font_size=25))
        self.img=Image(source='m2.jpg',)
        self.add_widget(self.img)
        self.message=Label(font_size=10)
        #self.add_widget(self.message)
        #self.add_widget(Label(text='the wenses media',font_size=10))

        self.search=Button(text='SEARCH',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.search)
        self.search.bind(on_press=self.going_search)

        self.news=Button(text='NEWS',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.news)

        self.chat=Button(text='CHATS',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.chat)
        self.chat.bind(on_press=self.chatting)

        self.settings=Button(text='SETTINGS',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.settings)
        self.settings.bind(on_press=self.go_to_settings)


        self.logout=Button(text='LOGOUT',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.logout)
        self.logout.bind(on_press=self.logging_out)

        self.buy=Button(text='BUYING PRODUCTS ONLINE',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.buy)

        self.forex=Button(text='FOREX',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.forex)
        self.forex.bind(on_press=self.forexing)

        self.bureau_de_change=Button(text='BUREAU DE CHANGE',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.bureau_de_change)
        self.bureau_de_change.bind(on_press=self.go_to_bdc)

        self.tuts=Button(text='BUSINESS TUTORIALS',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.tuts)

        self.exit=Button(text='EXIT',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.exit)
        self.exit.bind(on_press=self.exiting)

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

    def chatting(self,instance):
        sbc.screen_manager.current='chats'

    def forexing(self,instance):
        sbc.screen_manager.current='fx page'
        #plt.title('FOREX CHART')
        #x=(0,1,0)
        #y=(1,0,2)
        #plt.plot(x,y)
        #plt.ylabel('EUR/USD')
        #plt.xlabel('TIMELINE')
        #plt.show()


    def exiting(self,instance):
        exit()
    def update_info(self,message):
        self.message.text=message

    def go_to_bdc(self,instance):
        sbc.screen_manager.current='bdc'

    def logging_out(self,instance):
        sbc.screen_manager.current='main'

    def going_search(self,instance):
        sbc.screen_manager.current='search'

    def go_to_settings(self,instance):
        sbc.screen_manager.current='settings'




class SignUp(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='FILL OUT THE REQUIREMENTS',font_size=20))
        self.add_widget(Label(text='IN ORDER TO SIGN UP',font_size=20))

        #First Name
        self.add_widget(Label(text='First Name',font_size=15))
        self.first_name=TextInput(multiline=False)
        self.add_widget(self.first_name)

        #Last Name
        self.add_widget(Label(text='Last Name',font_size=15))
        self.last_name=TextInput(multiline=False)
        self.add_widget(self.last_name)

        #Email address
        self.add_widget(Label(text='Email',font_size=15))
        self.email=TextInput(multiline=False)
        self.add_widget(self.email)

        #Business role or position
        self.add_widget(Label(text='Business position',font_size=15))
        self.role=TextInput(multiline=False)
        self.add_widget(self.role)

        #Username
        self.add_widget(Label(text='Username',font_size=15))
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)

        #password
        self.add_widget(Label(text='Password',font_size=15))
        self.password=TextInput(multiline=False,)
        self.add_widget(self.password)

        #confirm password
        self.add_widget(Label(text='Confirm password',font_size=15,))
        self.confirm_password=TextInput(multiline=False)
        self.add_widget(self.confirm_password)

        self.back=Button(text='GO BACK',font_size=20,background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.go_back)

        self.next=Button(text='NEXT',font_size=20,background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.next)
        self.next.bind(on_press=self.go_next)

    def go_back(self,instance):
        sbc.screen_manager.current='main'

    def go_next(self,instance):
        global username1
        global password1
        username1=self.username.text
        password1=self.password.text
        name1=self.first_name.text
        name2=self.last_name.text
        username1=str(username1)
        password1=str(password1)
        name1=str(name1)
        name2=str(name2)
        if name1=='' and name2=='':
            sbc.screen_manager.current='error'
            Window.clearcolor=(1,0,0,1)
        else:

            sbc.screen_manager.current='signingup'

class SigningUp(GridLayout):
    def __init__(self,**kwargs):
        global username
        global password
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='CONGRATULATIONS YOU ARE ABOUT TO ',font_size=20))
        self.add_widget(Label(text='FINISH SETTING UP YOUR ACCOUNT',font_size=20))

        self.add_widget(Label(text='Your BIo'))
        self.bio=TextInput(multiline=False)
        self.add_widget(self.bio)

        self.add_widget(Label(text='Your Credit Card Number',))
        self.ccn=TextInput(multiline=False)
        self.add_widget(self.ccn)

        self.add_widget(Label(text='CVC',))
        self.cvc=TextInput(multiline=False)
        self.add_widget(self.cvc)

        self.add_widget(Label(text='Year of birth'))
        self.year=TextInput(multiline=False)
        self.add_widget(self.year)

        self.add_widget(Label(text='Nationality'))
        self.nation=TextInput(multiline=False)
        self.add_widget(self.nation)

        self.back=Button(text='GO BACK',font_size=20,background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.go_back)

        self.finish=Button(text='FINISH',font_size=20,background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.finish)
        self.finish.bind(on_press=self.do_finish)

    def go_back(self,instance):
        sbc.screen_manager.current='main'

    def do_finish(self,instance):
        global username1
        global password1
        if username1=='' and password1=='':
            sbc.screen_manager.current='error'
            Window.clearcolor=(1,0,0,1)
        else:

            sbc.home.update_info(username1)
            sbc.screen_manager.current='home'

class Search(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.search_i=TextInput(multiline=False)
        self.add_widget(self.search_i)

        self.add_widget(Label())


        self.search_button=Button(text='SEARCH',font_size=20,background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.search_button)
        self.search_button.bind(on_press=self.searching)

        self.add_widget(Label())
        self.add_widget(Label())

        self.back=Button(text='GO BACK TO HOMEPAGE',font_size=20,background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.gh)

    def searching(self,instance):
        input_query=self.search_i.text
        input_query=str(input_query)
        if input_query=='settings' or input_query=='Settings' or input_query=='SETTINGs':
            sbc.screen_manager.current='settings'
        elif input_query=='home' or input_query=='Home' or input_query=='HOME':
            sbc.screen_manager.current='home'
        #import sbc_searcher
        pd.set_option('display.max_colwidth',1)
        nlp=spacy.load('en_core_web_sm')
        df=pd.read_csv('sbc-b1.csv')

        text_list=df.Name.str.lower().values
        tok_text=[]

        for doc in tqdm(nlp.pipe(text_list, disable=['tagger','parser','ner'])):
            tok=[t.text for t in doc if t.is_alpha]
            tok_text.append(tok)

        bm25=BM25Okapi(tok_text)
        q=input_query
        tokq=q.lower().split(' ')

        t0=time.time()
        r=bm25.get_top_n(tokq, df.Name.values, n=3)
        t1=time.time() 

        for i in r:
            #print(i)
            sbc.sr.update_r(i)
            sbc.screen_manager.current='sr'
        


    def gh(self,instance):
        sbc.screen_manager.current='home'

class Sr(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(Label(text='SEARCH RESULTS'))

        self.r=Label(halign='center')
        self.add_widget(self.r)

    def update_r(self,r):
        self.r.text=r

class S(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=3

        self.add_widget(Label())
        self.add_widget(Label(text='SBC SETTINGS',font_size=20))
        self.add_widget(Label())

        self.uis=Button(text='USER INTERFACE SETTINGS',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.uis)
        self.uis.bind(on_press=self.go_to_ui)

        self.acs=Button(text='USER ACCOUNT SETTINGS',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.acs)
        self.acs.bind(on_press=self.uacst)

        self.ss=Button(text='SYSTEM SETTING',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.ss)

        self.back=Button(text='BACK TO HOMEPAGE',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.gh)

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

    def uacst(self,instance):
    	sbc.screen_manager.current='uacs'


    def gh(self,instance):
        sbc.screen_manager.current='home'

    def go_to_ui(self,instance):
        sbc.screen_manager.current='uis'


class Uisp(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='CHANGE BACKGROUND COLOR',font_size=20))
        self.add_widget(Label())

        self.red=Button(text='RED BACKGROUND COLOR',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.red)
        self.red.bind(on_press=self.change_to_red)

        self.blue=Button(text='BLUE BACKGROUND COLOR',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.blue)
        self.blue.bind(on_press=self.change_to_blue)

        self.purple=Button(text='PURPLE BACKGROUND COLOR',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.purple)
        self.purple.bind(on_press=self.change_to_purple)

        self.green=Button(text='GREEN BACKGROUND COLOR',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.green)
        self.green.bind(on_press=self.change_to_green)

        self.aqua=Button(text='LIGHT BLUE BACKGROUND COLOR',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.aqua)
        self.aqua.bind(on_press=self.change_to_aqua)

        self.black=Button(text='BLACK BACKGROUND COLOR',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.black)
        self.black.bind(on_press=self.change_to_black)

        self.add_widget(Label())

        self.back=Button(text='GO BACK TO HOME PAGE',font_size=15,background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.gh1)

    def change_to_black(self,instance):
        Window.clearcolor=(0,0,0,1)

    def change_to_aqua(self,instance):
        Window.clearcolor=(0,1,1,1)

    def change_to_purple(self,instance):
        Window.clearcolor=(1,0,1,1)

    def change_to_blue(self,instance):
        Window.clearcolor=(0,0,1,1)

    def change_to_green(self,instance):
        Window.clearcolor=(0,200/255.0,0,1)

    def gh1(self,instance):
        sbc.screen_manager.current='home'

    def change_to_red(self,instance):
        Window.clearcolor=(1,0,0,1)

class Bdc(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='Bureau',font_size=25))
        self.add_widget(Label(text='de change',font_size=25))

        self.add_widget(Label(text='Enter value in Tanzanian shillings:',))

        self.tsh=TextInput(multiline=False)
        self.add_widget(self.tsh)

        self.add_widget(Label(text='Convert to'))

        self.usd=Button(text='USD($)',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.usd)
        self.usd.bind(on_press=self.ch_usd)

        self.add_widget(Label())

        self.p=Button(text='Pounds Sterile',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.p)
        self.p.bind(on_press=self.ch_pounds)

        self.add_widget(Label())

        self.r=Button(text='Rand',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.r)
        self.r.bind(on_press=self.ch_rand)

        self.add_widget(Label())

        self.back=Button(text='GO BACK TO HOME PAGE',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.gh)

    def gh(self,instance):
        sbc.screen_manager.current='home'

    def ch_usd(self,instance):
        sh=self.tsh.text

        sh=int(sh)

        d=sh*0.00043
        print(d)
        ans=f'{sh} Tanzanian shillings is the same as {d} US dollars'
        sbc.bdc_usd.update_text(ans)
        sbc.screen_manager.current='bdcusd'

    def ch_pounds(self,instance):
        sh=self.tsh.text
        sh=int(sh)
        pound=sh*0.00032
        ans=f'{sh} shillings is the same as {pound} pounds'
        sbc.bdc_usd.update_text(ans)
        sbc.screen_manager.current='bdcusd'

    def ch_rand(self,instance):
        sh=self.tsh.text
        sh=int(sh)
        rand=sh*0.0066
        ans=f'{sh} shillings is the same as {rand} rand'
        sbc.bdc_usd.update_text(ans)
        sbc.screen_manager.current='bdcusd'

class Uacs(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label())
        self.add_widget(Label(text='USER ACCOUNT SETTINGS'))
        self.chp=Button(text='CHANGE PASSWORD',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.chp)
        self.add_widget(Label())
        self.chu=Button(text='CHANGE USERNAME',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.chu)
        self.add_widget(Label())
        self.aac=Button(text='ADD ANOTHER ACCOUNT',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.aac)
        self.add_widget(Label())
        self.bk=Button(text='GO BACK TO HOME PAGE',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.bk)
        self.bk.bind(on_press=self.gh)

    def gh(self,instance):
        sbc.screen_manager.current='home'

class BdcUsd(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.message=Label(font_size=15)
        self.add_widget(self.message)

        self.back=Button(text='GO BACK',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.gh)

        self.add_widget(Label())

    def gh(self,instance):
        sbc.screen_manager.current='bdc'

    def update_text(self,message):
        self.message.text=message

class FxPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2
        self.add_widget(Label())
        self.add_widget(Label(text='SBC FOREX LIVE',font_size=25))
        self.add_widget(Label())
        self.add_widget(Label(text='Enter the following requirements to get your forex chart'))
        #date timeline
        self.add_widget(Label(text='Enter date in DD/MM/YY format: '))
        self.date=TextInput(multiline=False)
        self.add_widget(self.date)

        #Currency
        self.add_widget(Label(text='Enter currency in C/C format: '))
        self.currency=TextInput(multiline=False)
        self.add_widget(self.currency)

        self.add_widget(Label())
        self.fxc=Button(text='DISPLAY REQUIRED FOREX CHART',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.fxc)
        self.fxc.bind(on_press=self.fx_chart)
        self.add_widget(Label())
        self.back=Button(text='GO BACK TO HOMEPAGE',background_color=(0,200/255.0,200/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.gh)

    def gh(self,instance):
        sbc.screen_manager.current='home'


    def fx_chart(self,instance):
        date=self.date.text
        currency=self.currency.text
        date=str(date)
        currency=str(currency)
        title=f'FOREX CHART AS AT {date}'
        plt.title(title)
        n1=random.randrange(150,500)
        n2=random.randrange(200,550)
        n3=random.randrange(700,850)
        x=(20,15,21)
        y=(n1,n2,n3)
        plt.plot(x,y)
        plt.ylabel(currency)
        plt.xlabel(date)
        plt.show()

class Chats(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2
        t=('')

        self.add_widget(Label(text='the wenses media>'))
        self.add_widget(Label(text=t))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.chtxt=TextInput(multiline=False,font_size=35)
        self.add_widget(self.chtxt)
        self.send=Button(text='SEND',background_color=(0,200/255.0,200/255.0,1),font_size=5)
        self.add_widget(self.send)

    def sending(self,instance):
        txt=self.chtxt.text



class SBCApp(App):
    def build(self):
        self.screen_manager=ScreenManager()

        self.main=Main()
        screen=Screen(name='main')
        screen.add_widget(self.main)
        self.screen_manager.add_widget(screen)

        #chatting page
        self.chats=Chats()
        screen=Screen(name='chats')
        screen.add_widget(self.chats)
        self.screen_manager.add_widget(screen)

        #forex page
        self.fx_page=FxPage()
        screen=Screen(name='fx page')
        screen.add_widget(self.fx_page)
        self.screen_manager.add_widget(screen)

        #search results
        self.sr=Sr()
        screen=Screen(name='sr')
        screen.add_widget(self.sr)
        self.screen_manager.add_widget(screen)


        #bdc
        self.bdc_usd=BdcUsd()
        screen=Screen(name='bdcusd')
        screen.add_widget(self.bdc_usd)
        self.screen_manager.add_widget(screen)

        self.uacs=Uacs()
        screen=Screen(name='uacs')
        screen.add_widget(self.uacs)
        self.screen_manager.add_widget(screen)

        self.home=Home()
        screen=Screen(name='home')
        screen.add_widget(self.home)
        self.screen_manager.add_widget(screen)

        self.log_in=Login()
        screen=Screen(name='login')
        screen.add_widget(self.log_in)
        self.screen_manager.add_widget(screen)

        self.error=Error()
        screen=Screen(name='error')
        screen.add_widget(self.error)
        self.screen_manager.add_widget(screen)

        self.sign_up=SignUp()
        screen=Screen(name='signup')
        screen.add_widget(self.sign_up)
        self.screen_manager.add_widget(screen)

        self.search=Search()
        screen=Screen(name='search')
        screen.add_widget(self.search)
        self.screen_manager.add_widget(screen)

        self.signing_up1=SigningUp()
        screen=Screen(name='signingup')
        screen.add_widget(self.signing_up1)
        self.screen_manager.add_widget(screen)

        self.sbc_settings=S()
        screen=Screen(name='settings')
        screen.add_widget(self.sbc_settings)
        self.screen_manager.add_widget(screen)

        self.uisp=Uisp()
        screen=Screen(name='uis')
        screen.add_widget(self.uisp)
        self.screen_manager.add_widget(screen)

        self.bdc=Bdc()
        screen=Screen(name='bdc')
        screen.add_widget(self.bdc)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__=="__main__":
    sbc=SBCApp()
    sbc.run()
