from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "System Of Equations Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "A Junice Industries Product"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to Continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "System Of Equations Calculator"   
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "System_Of_Equations"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit Junice Industries"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.juniceindustries.com/subscribe') 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 1000
                width: 1000
""")

Builder.load_string("""
<System_Of_Equations>
    id:System_Of_Equations
    name:"System_Of_Equations"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "System Of Equations Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()       
                        a_entry_eq1.text = ""
                        b_entry_eq1.text = ""
                        c_entry_eq1.text = "" 
                        a_entry_eq2.text = ""
                        b_entry_eq2.text = ""
                        c_entry_eq2.text = ""
                        
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "ax + by = c"
                
            BoxLayout:
                cols: 1
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                TextInput:
                    id: a_entry_eq1
                    text: a_entry_eq1.text
                    hint_text: "+/- a"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    text: "x"
                    
                TextInput:
                    id: b_entry_eq1
                    text: b_entry_eq1.text
                    hint_text: "+/- b"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    text: "y"
                    
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    text: "="
                    
                TextInput:
                    id: c_entry_eq1
                    text: c_entry_eq1.text
                    hint_text: "+/- c"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
            
            BoxLayout:
                cols: 1
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                TextInput:
                    id: a_entry_eq2
                    text: a_entry_eq2.text
                    hint_text: "+/- a"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    text: "x"
                    
                TextInput:
                    id: b_entry_eq2
                    text: b_entry_eq2.text
                    hint_text: "+/- b"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    text: "y"
                    
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    text: "="
                    
                TextInput:
                    id: c_entry_eq2
                    text: c_entry_eq2.text
                    hint_text: "+/- c"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200      
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    System_Of_Equations.steps(a_entry_eq1.text + "," + b_entry_eq1.text + "," + c_entry_eq1.text + "," + a_entry_eq2.text + "," + b_entry_eq2.text + "," + c_entry_eq2.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class System_Of_Equations(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(System_Of_Equations, self).__init__(**kwargs)
        
    layouts = []
    def steps(self,entry):
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
            entry_list = entry.split(",")
            #entry_list = entry_list.remove("")
            print("entry_list",entry_list)
            
            # Remove empty elements
            i = 0
            while i < len(entry_list):
                if entry_list[i] == '':
                    entry_list.pop(i)
                    print("entry_list removed empty element")
                    self.ids.list_of_steps.add_widget(Label(text= "Missing element!" ,font_size = '20sp', size_hint_y= None, height=100))
                i = i + 1
            
            # use the first 3 elements for equation1, the last 3 for equation2
            
            if len(entry_list) == 6:
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Entry List = 6, okay to use!")
                print()
                entry_list_Equation1 = entry_list[:3]
                print("entry_list_Equation1",entry_list_Equation1)
                
                equation1 = entry_list_Equation1[0].replace("+","").replace(" ","") + "x + " + entry_list_Equation1[1].replace(" ","") + "y = " + entry_list_Equation1[2].replace("+","").replace(" ","")
                equation1 = equation1.replace("+ -","- ")
                print(equation1)
                self.ids.list_of_steps.add_widget(Label(text= "Equation 1: " + equation1 ,font_size = '20sp', size_hint_y= None, height=100))
                
                entry_list_Equation2 = entry_list[3:]
                print("entry_list_Equation2",entry_list_Equation2)
                
                equation2 = entry_list_Equation2[0].replace("+","").replace(" ","") + "x + " + entry_list_Equation2[1].replace(" ","") + "y = " + entry_list_Equation2[2].replace("+","").replace(" ","")
                equation2 = equation2.replace("+ -","- ")
                print(equation2)
                self.ids.list_of_steps.add_widget(Label(text= "Equation 2: " + equation2 ,font_size = '20sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '20sp', size_hint_y= None, height=100))
                
                #Find if Elimination or Manipulation is needed to solve
                
                if float(entry_list_Equation1[0].replace("+","").replace(" ","")) + float(entry_list_Equation2[0].replace("+","").replace(" ","")) == 0.0:
                    print("Found elimination for variable A")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Solve by Elimination" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=ff3364]' + "Eliminate The Following" + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + "Add The Following" + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    variable_B_EQ1 = " + " + entry_list_Equation1[1].replace(" ","")
                    print("variable_B_EQ1: ",variable_B_EQ1)
                    variable_B_EQ1 = '[color=33CAFF]' + variable_B_EQ1.replace("+ -","- ") + '[/color]'
                    print("variable_B_EQ1 (with color!): ",variable_B_EQ1)
                    self.ids.list_of_steps.add_widget(Label(text= '[color=ff3364]' + entry_list_Equation1[0].replace("+","").replace(" ","") + "x" + '[/color]' + variable_B_EQ1 + "y = " + '[color=33CAFF]' + entry_list_Equation1[2].replace("+","").replace(" ","") + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    variable_B_EQ2 = " + " + entry_list_Equation2[1].replace(" ","")
                    print("variable_B_EQ2: ",variable_B_EQ2)
                    variable_B_EQ2 = '[color=33CAFF]' + variable_B_EQ2.replace("+ -","- ") + '[/color]'
                    print("variable_B_EQ2 (with color!): ",variable_B_EQ2)
                    self.ids.list_of_steps.add_widget(Label(text= '[color=ff3364]' + entry_list_Equation2[0].replace("+","").replace(" ","") + "x" + '[/color]' + variable_B_EQ2 + "y = " + '[color=33CAFF]' + entry_list_Equation2[2].replace("+","").replace(" ","") + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= " + ___________________________",font_size = '20sp', size_hint_y= None, height=10, markup=True))

                    constant_Y = entry_list_Equation1[1].replace(" ","") + " + "  + entry_list_Equation2[1].replace(" ","")
                    print('constant_Y: ',constant_Y)
                    constant_Y_solved = str(eval(constant_Y))
                    print("constant_Y_solved",constant_Y_solved)
                    
                    answer = entry_list_Equation1[2].replace(" ","") + " + "  + entry_list_Equation2[2].replace(" ","")
                    print('answer: ',answer)
                    answer_evaled = str(eval(answer))
                    print("answer_evaled",answer_evaled)

                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + constant_Y_solved + '[/color]' + "y = " + '[color=33CAFF]' + answer_evaled + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    y_equals = str(eval(str(answer_evaled + "/" + constant_Y_solved)))
                    print('y_equals: ',y_equals)

                    self.ids.list_of_steps.add_widget(Label(text= "y = " + '[color=33CAFF]' + y_equals + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Solved for y, Use Equation 1 to solve for x",font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    print()
                    print("Solving for X with equation1: ",equation1)
                    
                    equation1_with_y_equals = equation1.replace("y","*(" + y_equals + ")")
                    print("Equation 1 with y: ",equation1_with_y_equals)
                    
                    #find coefficient in front of x variable
                    equation1_with_y_equals_xcoef_index = equation1_with_y_equals.find('x')
                    print("equation1_with_y_equals_xcoef_index: ",equation1_with_y_equals_xcoef_index)
                    
                    acoef = equation1_with_y_equals[:equation1_with_y_equals_xcoef_index]
                    print("acoef: ",acoef)
                    
                    #Find equal sign index to locate ycoef and answer to solve for x
                    equal_sign_index = equation1_with_y_equals.find('=')
                    print("equal_sign_index: ",equal_sign_index)
                    
                    bcoef_yvar = equation1_with_y_equals[equation1_with_y_equals_xcoef_index+1:equal_sign_index]
                    print("bcoef_yvar: ",bcoef_yvar)
                    bcoef_yvar_evaled = "+ " + str(eval(str(bcoef_yvar)))
                    bcoef_yvar_evaled = bcoef_yvar_evaled.replace("+ -","- ")
                    print("bcoef_yvar_evaled: ",bcoef_yvar_evaled)
                    
                    answer_from_EQ1 = equation1_with_y_equals[equal_sign_index+1:]
                    print("answer_from_EQ1: ",answer_from_EQ1)
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(acoef) + "x " + '[color=33CAFF]' + str(bcoef_yvar) + '[/color]' + " = " + str(answer_from_EQ1),font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= str(acoef) + "x " + '[color=33CAFF]' + str(bcoef_yvar_evaled) + '[/color]' + " = " + str(answer_from_EQ1),font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    if bcoef_yvar_evaled.count("+") == 1:
                        print()
                        print("Found the plus sign, must subtract from both sides")
                        self.ids.list_of_steps.add_widget(Label(text= str(acoef) + "x " + '[color=33CAFF]' + str(bcoef_yvar_evaled) + '[/color]' + '[color=ff3364]' + " - " + str(bcoef_yvar_evaled).replace("+","") + '[/color]' + " = " + str(answer_from_EQ1) + '[color=ff3364]' + " - " + str(bcoef_yvar_evaled).replace("+","") + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                        
                        answer_bcoef_and_y_evaled = str(eval(str(str(answer_from_EQ1) + "-" + str(bcoef_yvar_evaled))))
                        print("answer_bcoef_and_y_evaled: ",answer_bcoef_and_y_evaled)
                        
                        self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + str(acoef) + '[/color]' + "x = " + '[color=33CAFF]' + str(answer_bcoef_and_y_evaled) + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                        
                        acoef_answer_bcoef_and_y_evaled = str(eval(str(str(answer_bcoef_and_y_evaled) + "/" + str(acoef))))
                        print("acoef_answer_bcoef_and_y_evaled: ",acoef_answer_bcoef_and_y_evaled)
                        self.ids.list_of_steps.add_widget(Label(text= "x = " + '[color=33CAFF]' + str(acoef_answer_bcoef_and_y_evaled) + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    else:
                        print()
                        print("Found the minus sign, must add from both sides")
                        self.ids.list_of_steps.add_widget(Label(text= str(acoef) + "x " + '[color=33CAFF]' + str(bcoef_yvar_evaled) + '[/color]' + '[color=ff3364]' + " + " + str(bcoef_yvar_evaled).replace("+","") + '[/color]' + " = " + str(answer_from_EQ1) + '[color=ff3364]' + " - " + str(bcoef_yvar_evaled).replace("+","") + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                        
                        answer_bcoef_and_y_evaled = str(eval(str(str(answer_from_EQ1) + "+" + str(bcoef_yvar_evaled))))
                        print("answer_bcoef_and_y_evaled: ",answer_bcoef_and_y_evaled)
                        
                        self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + str(acoef) + '[/color]' + "x = " + '[color=33CAFF]' + str(answer_bcoef_and_y_evaled) + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                        
                        acoef_answer_bcoef_and_y_evaled = str(eval(str(str(answer_bcoef_and_y_evaled) + "/" + str(acoef))))
                        print("acoef_answer_bcoef_and_y_evaled: ",acoef_answer_bcoef_and_y_evaled)
                        self.ids.list_of_steps.add_widget(Label(text= "x = " + '[color=33CAFF]' + str(acoef_answer_bcoef_and_y_evaled) + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Final Answer:",font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "x = " + '[color=33CAFF]' + str(acoef_answer_bcoef_and_y_evaled) + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "y = " + '[color=33CAFF]' + str(y_equals) + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                #Eliminate Y
                elif float(entry_list_Equation1[1].replace("+","").replace(" ","")) + float(entry_list_Equation2[1].replace("+","").replace(" ","")) == 0.0:
                    print("Found elimination for variable B")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Solve by Elimination" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=ff3364]' + "Eliminate The Following" + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + "Add The Following" + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    variable_b_EQ1 = "+ " + entry_list_Equation1[1]
                    print("variable_b_EQ1 : ",variable_b_EQ1)
                    variable_b_EQ1 = variable_b_EQ1.replace("+ -","- ")
                    print("variable_b_EQ1 cleaned: ",variable_b_EQ1)
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + entry_list_Equation1[0].replace("+","").replace(" ","") + "x " + '[/color]' + '[color=ff3364]' + variable_b_EQ1 + "y" + '[/color]' + " = "  + '[color=33CAFF]' + entry_list_Equation1[2].replace("+","").replace(" ","") + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    variable_b_EQ2 = "+ " + entry_list_Equation2[1]
                    print("variable_b_EQ2: ",variable_b_EQ2)
                    variable_b_EQ2 = variable_b_EQ2.replace("+ -","- ")
                    print("variable_b_EQ2 cleaned: ",variable_b_EQ2)
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + entry_list_Equation2[0].replace("+","").replace(" ","") + "x " + '[/color]' + '[color=ff3364]' + variable_b_EQ2 + "y" + '[/color]' + " = "  + '[color=33CAFF]' + entry_list_Equation2[2].replace("+","").replace(" ","") + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= " + ___________________________",font_size = '20sp', size_hint_y= None, height=10, markup=True))


                    constant_x = entry_list_Equation1[0].replace(" ","") + " + "  + entry_list_Equation2[0].replace(" ","")
                    print('constant_x: ',constant_x)
                    constant_x_solved = str(eval(constant_x))
                    print("constant_x_solved",constant_x_solved)
                    
                    answer = entry_list_Equation1[2].replace(" ","") + " + "  + entry_list_Equation2[2].replace(" ","")
                    print('answer: ',answer)
                    answer_evaled = str(eval(str(answer)))
                    print("answer_evaled",answer_evaled)

                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + constant_x_solved + '[/color]' + "x = " + '[color=33CAFF]' + answer_evaled + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    y_equals = str(eval(str(answer_evaled + "/" + constant_x_solved)))
                    print('y_equals: ',y_equals)

                    self.ids.list_of_steps.add_widget(Label(text= "x = " + '[color=33CAFF]' + y_equals + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Solved for x, Use Equation 1 to solve for y",font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    print()
                    print("Solving for Y with equation1: ",equation1)
                    
                    equation1_with_y_equals = equation1.replace("x","*(" + y_equals + ")")
                    print("Equation 1 with y: ",equation1_with_y_equals)
                    
                    #find coefficient in front of x variable
                    right_par = equation1_with_y_equals.find(')')
                    print("right_par: ",right_par)
                    
                    equal_sign = equation1_with_y_equals.find('=')
                    print("equal_sign: ",equal_sign)
                    
                    bcoef_xvar = equation1_with_y_equals[:right_par+1]
                    print("bcoef_xvar: ",bcoef_xvar)
                    
                    bcoef_xvar_evaled = str(eval(str(bcoef_xvar)))
                    print("bcoef_xvar_evaled: ",bcoef_xvar_evaled)
                    
                    bcoef_yvar = equation1_with_y_equals[right_par+1:equal_sign]
                    Y_index = bcoef_yvar.find("y")
                    bcoef = bcoef_yvar[:Y_index]
                    bcoef = bcoef.replace("+ -","- ")
                    print("bcoef: ",bcoef)
                    
                    answer = equation1_with_y_equals[equal_sign+1:]
                    print("answer: ",answer)

                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + bcoef_xvar + '[/color]' + bcoef + "y = " + answer,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + bcoef_xvar_evaled + '[/color]' + bcoef + "y = " + answer,font_size = '20sp', size_hint_y= None, height=100, markup=True))

                    if float(bcoef_xvar_evaled) >= 0.0:
                        print("Found positive number, subtract on both sides.")
                        self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + bcoef_xvar_evaled + '[/color]' + " - " + '[color=ff3364]' + bcoef_xvar_evaled + '[/color]' + bcoef + "y = " + answer + '[color=ff3364]' + " - " + bcoef_xvar_evaled + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                        
                        answer_minus_bcoef_xvar_evaled = str(eval(str(answer) + "-" + str(bcoef_xvar_evaled)))
                        print("answer_minus_bcoef_xvar_evaled: ",answer_minus_bcoef_xvar_evaled)
                        
                        self.ids.list_of_steps.add_widget(Label(text= bcoef + "y = " + '[color=33CAFF]' + answer_minus_bcoef_xvar_evaled + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))

                        y_equals = str(answer_minus_bcoef_xvar_evaled) + "/" + str(bcoef)
                        y_equals = str(eval(y_equals))
                        print("y_equals: ",y_equals)
                        
                        self.ids.list_of_steps.add_widget(Label(text= "y = " + '[color=33CAFF]' + y_equals + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))

                        
                    else:
                        print("Found negative number, add on both sides.")
                        self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + bcoef_xvar_evaled + '[/color]' + " - " + '[color=ff3364]' + bcoef_xvar_evaled + '[/color]' + bcoef + "y = " + answer + '[color=ff3364]' + " - " + bcoef_xvar_evaled + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                        
                        answer_minus_bcoef_xvar_evaled = str(eval(str(answer) + "+" + str(bcoef_xvar_evaled)))
                        print("answer_minus_bcoef_xvar_evaled: ",answer_minus_bcoef_xvar_evaled)
                        
                        self.ids.list_of_steps.add_widget(Label(text= bcoef + "y = " + '[color=33CAFF]' + answer_minus_bcoef_xvar_evaled + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))

                        y_equals = str(answer_minus_bcoef_xvar_evaled) + "/" + str(bcoef)
                        y_equals = str(eval(y_equals))
                        print("y_equals: ",y_equals)
                        
                        self.ids.list_of_steps.add_widget(Label(text= "y = " + '[color=33CAFF]' + y_equals + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                else: #Use Manipulation
                    print("Use Manipulation")
                    self.ids.list_of_steps.add_widget(Label(text= "Solve by Manipulation" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Take X coefficients, multiply each equation by the other X coefficient" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '20sp', size_hint_y= None, height=100))

                    equation1 = entry_list_Equation1[0].replace("+","").replace(" ","") + "x + " + entry_list_Equation1[1].replace(" ","") + "y = " + entry_list_Equation1[2].replace("+","").replace(" ","")
                    equation1 = equation1.replace("+ -","- ")
                    print(equation1)
                    self.ids.list_of_steps.add_widget(Label(text= "Equation 1: " + equation1 ,font_size = '20sp', size_hint_y= None, height=100))
                    
                    entry_list_Equation2 = entry_list[3:]
                    print("entry_list_Equation2",entry_list_Equation2)
                    
                    equation2 = entry_list_Equation2[0].replace("+","").replace(" ","") + "x + " + entry_list_Equation2[1].replace(" ","") + "y = " + entry_list_Equation2[2].replace("+","").replace(" ","")
                    equation2 = equation2.replace("+ -","- ")
                    print(equation2)
                    self.ids.list_of_steps.add_widget(Label(text= "Equation 2: " + equation2 ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '20sp', size_hint_y= None, height=100))
                    
                    #Check if equation1 X Coefficient is positive or negative and if equation2 X Coefficient is positive or negative
                    #If + , + : Flip Equation1 to Negative and leave Equation2 as Positive
                    #if - , + : DO NOT FLIP ANYTHING, just multiply!
                    #If + , - : DO NOT FLIP ANYTHING, just multiply!
                    #If - , - : Flip Equation1 to Positive and leave Equation2 as Negative 
                    print()
                    
                    if float(entry_list_Equation1[0].replace("+","").replace(" ","")) > 0 and float(entry_list_Equation2[0].replace("+","").replace(" ","")) > 0:
                        print("Found + , +")
                        print("Flip Equation1 to Negative and leave Equation2 as Positive")
                        manip1 = "-" + entry_list_Equation1[0].replace("+","").replace(" ","")
                        manip2 = entry_list_Equation2[0].replace("+","").replace(" ","")
                        
                    elif float(entry_list_Equation1[0].replace("+","").replace(" ","")) < 0 and float(entry_list_Equation2[0].replace("+","").replace(" ","")) < 0:
                        print("Found - , -")
                        print("Flip Equation1 to Positive and leave Equation2 as Negative")
                        manip1 = "+" + entry_list_Equation1[0].replace("+","").replace(" ","")
                        manip2 = entry_list_Equation2[0].replace("+","").replace(" ","")
                        
                    elif float(entry_list_Equation1[0].replace("+","").replace(" ","")) > 0 and float(entry_list_Equation2[0].replace("+","").replace(" ","")) < 0:
                        print("Found - , +")
                        print("DO NOT FLIP ANYTHING, just multiply!")
                        manip1 = entry_list_Equation1[0].replace("+","").replace(" ","")
                        manip2 = entry_list_Equation2[0].replace("+","").replace(" ","")
                        
                    elif float(entry_list_Equation1[0].replace("+","").replace(" ","")) < 0 and float(entry_list_Equation2[0].replace("+","").replace(" ","")) > 0:
                        print("Found + , -")
                        print("DO NOT FLIP ANYTHING, just multiply!")
                        manip1 = entry_list_Equation1[0].replace("+","").replace(" ","")
                        manip2 = entry_list_Equation2[0].replace("+","").replace(" ","")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Solve by Elimination" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + manip2 + '[/color]' + "(" + equation1 + ")" ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + manip1 + '[/color]' + "(" + equation2 + ")" ,font_size = '20sp', size_hint_y= None, height=100, markup=True))

                    # use Manip1 and Manip2 to multiply equations
                    
                    A_Coefficient_eq1 = str(eval(str(manip2 + "*" + entry_list_Equation1[0].replace("+","").replace(" ",""))))
                    B_Coefficient_eq1 = str(eval(str(manip2 + "*" + entry_list_Equation1[1].replace("+","").replace(" ",""))))
                    Answer_eq1 = str(eval(str(manip2 + "*" + entry_list_Equation1[2].replace("+","").replace(" ",""))))
                    
                    equation1 = str(A_Coefficient_eq1 + "x + " + B_Coefficient_eq1 + "y = " + Answer_eq1).replace("+ -","- ")
                    equation1_display = str('[color=ff3364]' + A_Coefficient_eq1 + "x " + '[/color]' + "  + " + '[color=33CAFF]' + B_Coefficient_eq1 + "y " + '[/color]' + " = " + '[color=33CAFF]' + Answer_eq1 + '[/color]')
                    print("equation1_display: ",equation1_display)
                    
                    A_Coefficient_eq2 = str(eval(str(manip1 + "*" + entry_list_Equation2[0].replace("+","").replace(" ",""))))
                    B_Coefficient_eq2 = str(eval(str(manip1 + "*" + entry_list_Equation2[1].replace("+","").replace(" ",""))))
                    Answer_eq2 = str(eval(str(manip1 + "*" + entry_list_Equation2[2].replace("+","").replace(" ",""))))
                    
                    equation2 = str(A_Coefficient_eq2 + "x + " + B_Coefficient_eq2 + "y = " + Answer_eq2).replace("+ -","- ")
                    equation2_display = str('[color=ff3364]' + A_Coefficient_eq2 + "x " + '[/color]' + "  + " + '[color=33CAFF]' + B_Coefficient_eq2 + "y " + '[/color]' + " = " + '[color=33CAFF]' + Answer_eq2 + '[/color]')
                    print("equation2_display: ",equation2_display)
                    print("Manipulated both equations!")
                    print("equation1: ",equation1)
                    print("equation2: ",equation2)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=ff3364]' + "Eliminate The Following" + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + "Add The Following" + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= equation1_display,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= equation2_display ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= " + ___________________________",font_size = '20sp', size_hint_y= None, height=10, markup=True))
                    
                    add_B_Coeff = str(eval(str(B_Coefficient_eq1 + "+" +B_Coefficient_eq2)))
                    print("add_B_Coeff: ",add_B_Coeff)
                    
                    added_answer = str(eval(str(Answer_eq1 + "+" + Answer_eq2)))
                    print("added_answer: ",added_answer)
                    
                    self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' +  add_B_Coeff + "y" + '[/color]' + " = " + added_answer + '[/color]' ,font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    y_equals = str(eval(str(added_answer + "/" + add_B_Coeff)))
                    print("y_equals: ",y_equals)
                    
                    if str(y_equals) == "-0.0":
                        y_equals = 0.0
                    
                    self.ids.list_of_steps.add_widget(Label(text= "y = " + '[color=33CAFF]' +  y_equals + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Solve for x with y plugged into equation 1",font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    equation1 = str(A_Coefficient_eq1 + "x + " + '[color=33CAFF]' +  B_Coefficient_eq1 + "(" + y_equals + '[/color]' + ") = " + Answer_eq1).replace("+ -","- ")
                    self.ids.list_of_steps.add_widget(Label(text= equation1.replace("+ -","- "),font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    B_Coeff_and_y_equals_evaled = str(eval(str(B_Coefficient_eq1 + "*" +y_equals)))
                    print("B_Coeff_and_y_equals_evaled: ",B_Coeff_and_y_equals_evaled)
                    
                    if str(B_Coeff_and_y_equals_evaled) == "-0.0":
                        B_Coeff_and_y_equals_evaled = 0.0
                    
                    equation1 = str(A_Coefficient_eq1 + "x + " + '[color=33CAFF]' +  B_Coeff_and_y_equals_evaled + '[/color]' + " = " + Answer_eq1).replace("+ -","- ")
                    self.ids.list_of_steps.add_widget(Label(text= equation1.replace("+ -","- "),font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    Answer_eq1__dividedby__B_Coeff_and_y_equals_evaled = str(eval(str(Answer_eq1+"/"+B_Coeff_and_y_equals_evaled)))
                    print("Answer_eq1__dividedby__B_Coeff_and_y_equals_evaled: ",Answer_eq1__dividedby__B_Coeff_and_y_equals_evaled)
                    equation1 = str(A_Coefficient_eq1 + "x" + " = " + '[color=33CAFF]' +  Answer_eq1__dividedby__B_Coeff_and_y_equals_evaled + '[/color]').replace("+ -","- ")
                    self.ids.list_of_steps.add_widget(Label(text= equation1.replace("+ -","- "),font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    
                    x_equals = str(eval(str(Answer_eq1__dividedby__B_Coeff_and_y_equals_evaled+"/"+A_Coefficient_eq1)))
                    print("x_equals: ",x_equals)
                    self.ids.list_of_steps.add_widget(Label(text= "x = " + '[color=33CAFF]' + x_equals + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "x = " + '[color=33CAFF]' + str(x_equals) + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
                    self.ids.list_of_steps.add_widget(Label(text= "y = " + '[color=33CAFF]' + str(y_equals) + '[/color]',font_size = '20sp', size_hint_y= None, height=100, markup=True))
            else:
                print("CANNOT USE ENTRY LIST, NOT LENGTH OF 6")
                print("Length of entry_list = ",str(len(entry_list)))
                
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(System_Of_Equations(name="System_Of_Equations"))     
sm.current = "Homepage"   

class System_Of_Equations(App):
    def __init__(self, **kwargs):
        super(System_Of_Equations, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm
    
if __name__ == '__main__':
    System_Of_Equations().run()
    
