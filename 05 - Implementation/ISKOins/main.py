'''
MIT License
Copyright (c) 2017 Deanne C. Caingat, Lois M. Velasco, Eunice Cruz
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
This is a course requirement for CS192 Software Engineering II
under the supervision of Asst. Prof. Ma.Rowena C. Solamo 
of the Department of Computer Science, College of Engineering,
University of the Philippines, Diliman for the AY 2016-2017

Code History:

January 31, 2017 -- Deanne Caingat
Initial software
Add details

February 2,2017 -- Lois Velasco
add details error handling
reset details (no error handling yet)


February 13, 2017 -- Deanne Caingat
reset details error handling
add details proper input (init_amt>total amount for all categories)
show_popup function

February 16, 2017 -- Lois Velasco
Add Budget Details (different implementation)
Add Expense Details
Error Handling for some cases i.e, edit budget details, display, add expense details


April 6, 2017 -- Lois Velasco
Placed the graphs in main menu
Fixed Layout
Changed the Expense Part of Main Menu Screen

Clariz O. Caingat is credited for making the icons of the categories.

File created on January 26,2017.
Developed by DEL-TA group.
This software serves as the primary Class that integrates the modules. 
Software Project (ISKOins).
'''

import json
import os
import os.path
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
#from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import OptionProperty, StringProperty, NumericProperty, ListProperty

class MyBoxLayout(BoxLayout):
    pass

class MyCanvas1 (Label):
    bcolor = ObjectProperty([])
    bcolor1 = NumericProperty(0)
    bcolor2 = ObjectProperty([])
    bcolor3 = NumericProperty(0)
    label = StringProperty('')
    percentage = NumericProperty(0)

class Image (Label):
    source = StringProperty('')

class Wid (Widget):
    bcolor = ObjectProperty([])
    bcolor1 = NumericProperty(0)
    bcolor2 = ObjectProperty([])
    bcolor3 = NumericProperty(0)
    label = StringProperty('')
    percentage = NumericProperty(0)
class MyLabel2 (Label):
    image = ObjectProperty()

class MyLabel4 (Label):
    image = ObjectProperty()

class MyLabel (Label):
    image = ObjectProperty()

class MyLabel3 (Label):
    image = ObjectProperty()
class CustomButton (Label):
    pass

class NumberInput(TextInput):
    pass

'''
Function Name: show_popup
Creation Date: February 8,2017
Purpose: Generalized function in showing the popup. 
'''
def show_popup(p_label,p_title): #LOIS HALP LALAGYAN DIN BA TO NG METHOD NAME BLABLA HAHA ITO YUNG FUNCTION NA PANG SHOW NG POPUP LIKE U WANTED HUE
    pop_content = BoxLayout(orientation = 'vertical')
    pop_close = Button(text = 'Close', size_hint_y=0.5)
    pop_label = Label(text = p_label, valign='middle', halign='center')
    pop_label.bind(size=pop_label.setter("text_size"))
    pop_content.add_widget(pop_label)
    pop_content.add_widget(pop_close)
    p = Popup(title = p_title, auto_dismiss = False, content = pop_content, size_hint=(0.7, 0.3))
    pop_close.bind(on_press = p.dismiss)
    p.open()

class ScreenManagement(ScreenManager):
    pass

class StartUPScreen(Screen):
    '''
    Function Name: show_popup
    Creation Date: April 6, 2017
    Purpose: Shows the AboutUS PopUP on opening screen
    '''
    def aboutPopUP (self):
        pop_content = BoxLayout(orientation = 'vertical')
        pop_close = Button(text = 'Close', size_hint=(0.5,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        p_content = "This is a course requirement for CS192 Software Engineering II under the supervision of Asst. Prof. Ma.Rowena C. Solamo  of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2016-2017\n\n Developers:\n Eunice Angel D. Cruz \n Deanne Faye C. Caingat \n Lois Alexis M. Velasco \n\n Image Credits:\n Clariz O. Caingat\n Icons by Freepik and DotOnPaper from www.flaticons.com\n\nDate Finished: 30 April 2017"
        pop_label = Label(text = p_content, valign='middle', halign='center')
        pop_label.bind(size=pop_label.setter("text_size"))
        pop_content.add_widget(pop_label)
        pop_content.add_widget(pop_close)
        p = Popup(title = "About this Application", auto_dismiss = False, content = pop_content, size_hint=(0.8, 0.75))
        pop_close.bind(on_press = p.dismiss)
        p.open()


class MainScreen(Screen):      
    '''
    Function: Initializer
    Creation Date: April 5,2017
    Purpose: So that the values/labels can be changed when necessary 
    Required file: "output.txt"
    '''
    if os.path.exists('output.txt'):
        with open('output.txt','r') as json_data:
                data=json.load(json_data)
        labelText1 = NumericProperty((data['details']['init_amt']))
        labelText2 = NumericProperty((data['details']['total_expense']))
        labelText3 = NumericProperty((data['details']['init_amt'])-(data['details']['total_expense']))
        budget1 = NumericProperty(data['budget']['Food'])
        budget2 = NumericProperty(data['budget']['Transportation'])
        budget3 = NumericProperty(data['budget']['Groceries'])
        budget4 = NumericProperty(data['budget']['Health'])
        budget5 = NumericProperty(data['budget']['Laundry'])
        budget6 = NumericProperty(data['budget']['Supplies'])
        budget7 = NumericProperty(data['budget']['Dorm Fee'])
        budget8 = NumericProperty(data['budget']['Savings'])
        expense1 = NumericProperty(data['expenses']['Food'])
        expense2 = NumericProperty(data['expenses']['Transportation'])
        expense3 = NumericProperty(data['expenses']['Groceries'])
        expense4 = NumericProperty(data['expenses']['Health'])
        expense5 = NumericProperty(data['expenses']['Laundry'])
        expense6 = NumericProperty(data['expenses']['Supplies'])
        expense7 = NumericProperty(data['expenses']['Dorm Fee'])
        expense8 = NumericProperty(data['expenses']['Savings'])
    else:
        labelText1 = NumericProperty(0.00)
        labelText2 = NumericProperty(0.00)
        labelText3 = NumericProperty(0.00)
        budget1 = NumericProperty(0.00)
        budget2 = NumericProperty(0.00)
        budget3 = NumericProperty(0.00)
        budget4 = NumericProperty(0.00)
        budget5 = NumericProperty(0.00)
        budget6 = NumericProperty(0.00)
        budget7 = NumericProperty(0.00)
        budget8 = NumericProperty(0.00)
        expense1 = NumericProperty(0.00)
        expense2 = NumericProperty(0.00)
        expense3 = NumericProperty(0.00)
        expense4 = NumericProperty(0.00)
        expense5 = NumericProperty(0.00)
        expense6 = NumericProperty(0.00)
        expense7 = NumericProperty(0.00)
        expense8 = NumericProperty(0.00)

    '''
    Method Name: addExpenseScreen
    Creation Date: February 16,2017
    Purpose: Allows the user to add expense details once budget details exists. shows an error message otherwise.
    Required file: "output.txt"
    '''
    def addExpenseScreen(self):
        if (not os.path.exists("output.txt") or os.stat("output.txt").st_size==0):
            print "isEmpty"
            show_popup('No account found. Please create an account first.','Oooooops!')     
        else:
            self.parent.current='AddExpense'     

    '''
    Method Name: createAccount
    Creation Date: February 8,2017
    Purpose: Checks if there is a preexisting data. Shows an error message that only one account may be created.
    Required file: "output.txt"
    '''
    def createAccount(self):
        if (not os.path.exists("output.txt") or os.stat("output.txt").st_size==0):
            print "isEmpty"
            ISKOins.get_screen('CreateAccount').account = "NEW ACCOUNT"
            self.parent.current = 'CreateAccount'
        else:
            print "not isEmpty"         
            p_label = 'You can only have one account. Delete existing account to create a new one.'
            p_title = 'Error'
            show_popup(p_label,p_title)
            self.parent.current='Main'
    '''
    Method Name: editAccount
    Creation Date: February 16,2017
    Purpose: Checks if there is a preexisting data and brings the user to EditAccountScreen it once data exists. Shows an error message otherwise. 
    Required file: "output.txt"
    '''
    def editAccount(self):
        if (not os.path.exists("output.txt") or os.stat("output.txt").st_size==0):
            p_label = 'Nonexistent account. We cannot edit anything'
            p_title = 'Error'
            show_popup(p_label,p_title)
            self.parent.current='Main'
        else:
            ISKOins.get_screen('CreateAccount').account = "EDIT ACCOUNT"
            self.parent.current='CreateAccount'
    
    '''
    Method Name: deletion
    Creation Date: February 2,2017
    Purpose: deletes existing budget details
    Required file: "output.txt"
    '''  
    def deletion(self):
        if os.path.exists('output.txt'):
            os.remove('output.txt')
            show_popup('Account Deleted!','Success')
            MainScreen().labelReset()
            MainScreen().labelTextChangeFunc(str(0),str(0),str(0))
        else:
            print "No account created yet."
            show_popup('No account found. Please create an account first.','Oooooops!') 

    '''
    Method Name: deleteAccount
    Creation Date: February 2,2017
    Purpose: Prompts user if s/he wants to delete file; Driver for deletion of budget details
    Required file: "output.txt"
    '''  
    def deleteAccount(self):
        pop_content = BoxLayout(orientation = 'vertical')
        pop_ok = Button(text = 'DELETE', size_hint_y=0.25)
        pop_cancel = Button(text = 'CANCEL', size_hint_y=0.25)
        pop_label = Label(text = 'Are you sure you want to delete your account? This action cannot be undone.', valign='middle', halign='center')
        pop_label.bind(size=pop_label.setter("text_size"))
        pop_content.add_widget(pop_label)
       # pop_choices = BoxLayout (orientation = 'horizontal', size_hint_y=0.5)
        pop_content.add_widget(pop_ok)
        pop_content.add_widget(pop_cancel)
      # pop_content.add_widget(pop_choices)
        p = Popup(title = 'Delete Budget Details', auto_dismiss = False, content = pop_content, size_hint=(0.7, 0.3))
        pop_ok.bind(on_press = lambda x: self.deletion(), on_release = p.dismiss)
        pop_cancel.bind(on_press = p.dismiss)
        p.open()

    '''
    Method Name: labelTextChangeFunc
    Creation Date: April 5,2017
    Purpose: Changes the Labels on the account details part of the MainScreen
    '''  
    def labelTextChangeFunc (self, label1, label2, label3):
        ISKOins.get_screen('Main').labelText1 = label1
        ISKOins.get_screen('Main').labelText2 = label2
        ISKOins.get_screen('Main').labelText3 = label3

    '''
    Method Name: labelTextChangeFunction
    Creation Date: April 5,2017
    Purpose: Changes the Labels on the expense details part of the MainScreen
    '''  
    def labelTextChangeFunction (self):
        with open('output.txt  ','r') as json_data:
            data=json.load(json_data)
        ISKOins.get_screen('Main').budget1 = ((data['budget']['Food']))
        ISKOins.get_screen('Main').budget2 = ((data['budget']['Transportation']))
        ISKOins.get_screen('Main').budget3 = ((data['budget']['Groceries']))
        ISKOins.get_screen('Main').budget5 = ((data['budget']['Health']))
        ISKOins.get_screen('Main').budget6 = ((data['budget']['Laundry']))
        ISKOins.get_screen('Main').budget4 = ((data['budget']['Supplies']))
        ISKOins.get_screen('Main').budget7 = ((data['budget']['Dorm Fee']))
        ISKOins.get_screen('Main').budget8 = ((data['budget']['Savings']))
        ISKOins.get_screen('Main').expense1 = ((data['expenses']['Food']))
        ISKOins.get_screen('Main').expense2 = ((data['expenses']['Transportation']))
        ISKOins.get_screen('Main').expense3 = ((data['expenses']['Groceries']))
        ISKOins.get_screen('Main').expense5 = ((data['expenses']['Health']))
        ISKOins.get_screen('Main').expense6 = ((data['expenses']['Laundry']))
        ISKOins.get_screen('Main').expense4 = ((data['expenses']['Supplies']))
        ISKOins.get_screen('Main').expense7 = ((data['expenses']['Dorm Fee']))
        ISKOins.get_screen('Main').expense8 = ((data['expenses']['Savings']))

    '''
    Method Name: labelReset
    Creation Date: April 5,2017
    Purpose: Resets the Labels on the account details part of the MainScreen to 0.
    '''  
    def labelReset(self):
        ISKOins.get_screen('Main').budget1 = 0.00
        ISKOins.get_screen('Main').budget2 = 0.00
        ISKOins.get_screen('Main').budget3 = 0.00
        ISKOins.get_screen('Main').budget5 = 0.00
        ISKOins.get_screen('Main').budget4 = 0.00
        ISKOins.get_screen('Main').budget6 = 0.00
        ISKOins.get_screen('Main').budget7 = 0.00
        ISKOins.get_screen('Main').budget8 = 0.00
        ISKOins.get_screen('Main').expense1 = 0.00
        ISKOins.get_screen('Main').expense2 = 0.00
        ISKOins.get_screen('Main').expense3 = 0.00
        ISKOins.get_screen('Main').expense5 = 0.00
        ISKOins.get_screen('Main').expense6 = 0.00
        ISKOins.get_screen('Main').expense4 = 0.00
        ISKOins.get_screen('Main').expense7 = 0.00
        ISKOins.get_screen('Main').expense8 = 0.00
    
    '''
    Method Name: exitApplicationi
    Creation Date: February 14, 2017
    Purpose: exits the Application
    '''  
    def exitApplication(self):
        #something
        exit()

    '''
    Method Name: showWalletMENU
    Creation Date: April 1,2017
    Purpose: Proposed Wallet Menu --- AIMS to show a budget summary with pie graph -> expenses v. whole budget -- NOT USED;
    '''  
    def showWalletMENU(self):
        pop_content = BoxLayout(orientation = 'vertical', padding=(0,20,0,20), spacing='15dp')
        pop_summary = Button(text = 'View Budget Summary', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_addExpense = Button(text = 'Add Expense Details', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_close = Button(text = 'Close', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_content.add_widget(pop_summary)
        pop_content.add_widget(pop_addExpense)
        pop_content.add_widget(pop_close)
        p = Popup(title = "Wallet Menu", background='', title_color = (1,0,0,1), title_size = '20sp', separator_color = (1,0,0,1) , title_align = 'center', halign = 'center',auto_dismiss = False, content = pop_content, size_hint=(0.8, 0.45))
        pop_close.bind(on_press = p.dismiss)
        pop_summary.bind(on_press = lambda x: self.showSummary(), on_release = p.dismiss)
        pop_addExpense.bind(on_press = lambda x: self.addExpenseScreen(), on_release = p.dismiss)
        p.open()

    '''
    Method Name: showAccountMENU
    Creation Date: April 1,2017
    Purpose: POPUP MENU for the ACCOUNT -- Contains buttons to add,edit,delete account and exit app
    '''  
    def showAccountMENU(self):
        pop_content = BoxLayout(orientation = 'vertical', padding=(10,30,10,30), spacing='20dp')
        pop_createAccount = Button(text = 'Create Account', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_editAccount = Button(text = 'Edit Account', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_deleteAccount = Button(text = 'Delete Account', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_exitApplication = Button(text = 'Exit Application', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_close = Button(text = 'Close', size_hint=(0.8,0.1), halign='center', pos_hint= {'center_x': 0.5, 'center_y': 0.23})
        pop_content.add_widget(pop_createAccount)
        pop_content.add_widget(pop_editAccount)
        pop_content.add_widget(pop_deleteAccount)
        pop_content.add_widget(pop_exitApplication)
        pop_content.add_widget(pop_close)
        p = Popup(title = "account menu", title_font= 'varsity_regular.ttf', background='', title_color = (0.5,0,0,1), title_size = '20sp', separator_color = (0.5,0,0,1) , title_align = 'center', halign = 'center',auto_dismiss = False, content = pop_content, size_hint=(0.8, 0.7))
        pop_close.bind(on_press = p.dismiss)
        pop_createAccount.bind(on_press = lambda x: self.createAccount(), on_release = p.dismiss)
        pop_editAccount.bind(on_press = lambda x: self.editAccount(), on_release = p.dismiss)
        pop_deleteAccount.bind(on_press = lambda x: self.deleteAccount(), on_release = p.dismiss)
        pop_exitApplication.bind(on_press = lambda x: self.exitApplication(), on_release = p.dismiss)
        p.open()

class CreateAccountScreen(Screen):
    account = StringProperty('')
    '''
    Method Name: CreateAccount
    Creation Date: February 1,2017 -- Edited: April 3, 2017
    Purpose: Checks if there is incomplete budget details and if init_amt> per   cat.  Proceeds to save it otherwise/
    Update: Checks if there is incomplete account details [name, duration, Initial_amt] then assumes that input is 0 if left blank
    Required file: "output.txt"
    '''
    def CreateAccount(self,duration,name,init_amt,Food,Transportation,Groceries,Supplies,Health,Laundry,DormFee,Savings):
        print "CreateAccount"
        error=0
        suma = 0
        List = [name,init_amt,duration,Food,Transportation,Groceries,Supplies,Health,Laundry,DormFee,Savings] #list of user input
        for items in  List[0:3]:
            print items
            if items=="":
                error=1
        for x in range(3,11):
            if List[x] == "":
                List[x]=float(0)
            else:
                List[x]=float(List[x])
                suma = suma+List[x]

        if init_amt!="" and int(init_amt) < suma:
            error=2
        if error==0:
            account = {}
            account ['details'] = {'name': name, 'init_amt': float(init_amt), 'duration':duration, 'total_expense':0.00}
            account ['budget'] ={'Food':List[3], 'Transportation':List[4], 'Groceries':List[5], 'Supplies':List[6], 'Health':List[7], 'Laundry':List[8], 'Dorm Fee':List[9], 'Savings':List[10]}
            account ['expenses'] ={'Food':0.00, 'Transportation':0.00, 'Groceries':0.00, 'Supplies':0.00, 'Health':0.00, 'Laundry':0.00, 'Dorm Fee':0.00, 'Savings':0.00}           
            s=json.dumps(account)
            with open ("output.txt","w") as f:
                f.write(s)
            p_title='Success'
            p_label='Recorded'
            show_popup(p_label, p_title)
            text1 = account['details']['init_amt']
            text2 = account['details']['total_expense']
            MainScreen().labelTextChangeFunc((text1), (0.00), (float(text1 - text2)))
            MainScreen().labelTextChangeFunction()
            self.parent.current='Main'
        elif error==2 :
            print   "Error"
            p_label = 'Initial amount is less than the total amount allocated for categories'
            p_title = 'Error'
            show_popup(p_label,p_title) 
            self.parent.current='CreateAccount'
        else:
            print "Error: Some Fields were left blank"
            p_label = 'Please fill up account information'
            p_title = 'Oooooops'
            show_popup(p_label,p_title)
            self.parent.current='CreateAccount'

    '''
    Method Name: EditAccount
    Creation Date: April 3, 2017
    Purpose: Edits the budget details of the account but not the expenses part.
    Required file: "output.txt"
    '''
    def EditAccount(self,duration,name,init_amt,Food,Transportation,Groceries,Supplies,Health,Laundry,DormFee,Savings):
        print "Edit Account"
        error = 0
        suma = 0
        List = [name,init_amt,duration,Food,Transportation,Groceries,Supplies,Health,Laundry,DormFee,Savings] #list of user input
        List2 = ['name','init_amt','duration','Food','Transportation','Groceries','Supplies','Health','Laundry','Dorm Fee','Savings']
        with open('output.txt  ','r') as json_data:
            data=json.load(json_data)
        for x in range (3,11):
            if (List[x]!=""):
                List[x]=float(List[x])
                suma = suma+List[x]
            else:
                List[x]=float(0)
        if init_amt!="" and int(init_amt) < suma:
            error=2
        if error==0 and (not (List[0]=="" or List[1]=="")):
            data['details'][List2[0]]=List[0]
            data['details'][List2[1]]=float(List[1])
            data['details'][List2[2]]=List[2]
            for x in range (3,11):
                if (List[x]!=""):
                    data['budget'][List2[x]] = float(List[x])
                else:
                   data['budget'][List2[x]]=0 
            with open('output.txt', 'w') as json_data:
                json_data.write(json.dumps(data))
            p_title='Success'
            p_label='Recorded'
            show_popup(p_label, p_title)
            text1 = float(List[1])
            MainScreen().labelTextChangeFunc(text1, (data['details']['total_expense']), (int(text1) - data['details']['total_expense']))
            MainScreen().labelTextChangeFunction()
            self.parent.current='Main'
        elif error==2 :
            print   "error"
            p_label = 'Initial amount is less than the total amount allocated for categories'
            p_title = 'Error'
            show_popup(p_label,p_title) 
            self.parent.current='CreateAccount'
        else:
            print "Error: Some Fields were left blank"
            p_label = 'Please fill up account information'
            p_title = 'Oooooops'
            show_popup(p_label,p_title)

class AddExpenseScreen(Screen): 

    '''
    Method Name: get_expense_input
    Creation Date: February 16,2017
    Purpose: Shows a popup that will ask for user expense input of a selected category
    Required file: "output.txt"
    '''
    def get_expense_input(self, name):
        print "HOHO"
        print name
        pop_content = BoxLayout(orientation = 'vertical')
        pop_ok = Button(text = 'OK', size_hint_y=0.5)
        pop_cancel = Button(text = 'CANCEL', size_hint_y=0.5)
        label = 'Enter the Expense Amount' if (name!='Savings') else 'Enter the Savings Amount'
        pop_label = Label(text = label )
        pop_input = TextInput(input_type="number")
        pop_content.add_widget(pop_label)
        pop_content.add_widget(pop_input)
        pop_content.add_widget(pop_ok)
        pop_content.add_widget(pop_cancel)
        add = " expenses" if (name!='Savings') else ""
        p = Popup(title = name+add, auto_dismiss = False, content = pop_content, size_hint=(0.7, 0.3))
        #pop_ok.bind(on_press = self.something2(pop_input.text), on_release = p.dismiss)
        pop_ok.bind(on_press=lambda x:self.expense_write(name, pop_input.text), on_release = p.dismiss)
        pop_cancel.bind(on_press = p.dismiss)
        p.open()
    
    '''
    Method Name: expense_write 
    Creation Date: February 14,2017
    Purpose: Writes the expense details onto the output file.
    Required file: "output.txt"
    '''
    def expense_write(self,name,value):
        with open('output.txt  ','r') as json_data:
            value = 0 if (value == "") else float(value)
            data=json.load(json_data)
            if (data['details']['total_expense'])+float(value)<=(data['details']['init_amt']):
                if (data['details']['total_expense'])+float(value)>=(data['details']['init_amt']*0.80):
                    p_title = "Reminder"
                    p_label = "Expenses reached 80% of the initial budget allocated"
                    show_popup(p_label, p_title)
                    show_popup('Expense Details Added!','Success')
                else:
                    show_popup('Expense Details Added!','Success')
                data['expenses'][name]=(data['expenses'][name])+float(value)
                data['details']['total_expense']=(data['details']['total_expense'])+float(value)
                print data['details']['total_expense']
            else:
                p_title = "Error"
                p_label = "Expenses exceeded initial amount. Expense details cannot be added anymore."
                show_popup(p_label, p_title)
        with open('output.txt', 'w') as json_data:
            json_data.write(json.dumps(data))
        print "----------------"
        with open('output.txt','r') as json_data:
            data=json.load(json_data)
        print data['details']['total_expense']
        #MainScreen().load()
        

    '''
    Method Name: setText
    Creation Date: March 22,2017
    Purpose: Changes the labels total_expense and remaining balance in the MainScreen
    Required file: "output.txt"
    '''
    def setText(self):
        with open('output.txt','r') as json_data:
            data=json.load(json_data)
        text1 = (data['details']['init_amt'])
        text2 = (data['details']['total_expense'])
        text3 = (data['details']['init_amt']-data['details']['total_expense'])
        #self.manager.get_screen('Main').labelText2 = text2
        #self.manager.get_screen('Main').labelText3 = text3
        MainScreen().labelTextChangeFunc(text1, text2, text3)
        MainScreen().labelTextChangeFunction()

        self.manager.current = 'Main'

ISKOins = Builder.load_file('ISKOins3.kv')

class TestApp(App):

    def exit(self):
        exit()

    def build(self):
        return ISKOins

if __name__ == '__main__':
    TestApp().run() 
