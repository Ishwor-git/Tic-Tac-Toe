
import tkinter as tk
click_count = 0

main = { 'r4c0' : 0, 'r4c1' : 3, 'r4c2' : 6,
         'r5c0' : 1, 'r5c1' : 4, 'r5c2' : 7,
         'r6c0' : 2, 'r6c1' : 5, 'r6c2' : 8
}


def buttons(row,column):
    b1 = tk.Button(root,width = 4,height = 1, font = ('calibri',20,'bold'),justify = 'center',bg = 'darkgrey',fg = 'black')
    b1['command'] = lambda: click(row,column,b1)
    b1.grid(row = row,column = column, padx = 3, pady = 3, ipady = 1)
    return b1
def remark(text,color):
    return tk.Label(root,width = 12,height = 1,text = text,font = ('monotype corsiva',23),fg = color,bg = 'silver').grid(row = 8, column = 0, columnspan = 3, pady = 4,ipadx = 8,ipady = 3)

def label(row,column,text,color,bg = 'darkgrey'):
        return tk.Label(root, width=4, height=1,text = text, font=('calibri', 20, 'bold'), justify='center', bg=bg,fg=color).grid(row=row, column=column, padx=3, pady=4, ipady=10)

def output(row,column,text):
    if text == 'O':
        return label(row,column,text,'lime')
    else:
        return label(row,column,text,'red')

def test(var):
    if var == 'O':
        return remark('Player 1 is winner!'.format(var), 'forestgreen')
    else:
        return remark('player 2 is winner!'.format(var), 'firebrick')

def test_2(row,col,var):
    if var == 'O':
        label(row, col, None, None, 'forestgreen')
    else:
        label(row, col, None, None, 'firebrick')

def dictonary(row,column,var):
    global main
    main['r{0}c{1}'.format(row,column)] = var

    if main['r4c0'] == main['r4c1'] == main['r4c2']:
        test(var)
        test_2(4, 0, var)
        test_2(4, 1, var)
        test_2(4, 2, var)

    elif main['r5c0'] == main['r5c1'] == main['r5c2']:
        test(var)
        test_2(5, 0, var)
        test_2(5, 1, var)
        test_2(5, 2, var)

    elif main['r6c0'] == main['r6c1'] == main['r6c2']:
         test(var)
         test_2(6, 0, var)
         test_2(6, 1, var)
         test_2(6, 2, var)


    elif main['r4c0'] == main['r5c0'] == main['r6c0']:
        test(var)
        test_2(4, 0, var)
        test_2(5, 0, var)
        test_2(6, 0, var)

    elif main['r4c1'] == main['r5c1'] == main['r6c1']:
        test(var)
        test_2(4, 1, var)
        test_2(5, 1, var)
        test_2(6, 1, var)

    elif main['r4c2'] == main['r5c2'] == main['r6c2']:
        test(var)
        test_2(4, 2, var)
        test_2(5, 2, var)
        test_2(6, 2, var)


    elif main['r4c0'] == main['r5c1'] == main['r6c2']:
        test(var)
        test_2(4, 0, var)
        test_2(5, 1, var)
        test_2(6, 2, var)

    elif main['r4c2'] == main['r5c1'] == main['r6c0']:
        test(var)
        test_2(4, 2, var)
        test_2(5, 1, var)
        test_2(6, 0, var)
    else:
        pass

def click(row,column,obj):

    obj.destroy()
    global click_count
    if click_count % 2 == 0:
        output(row,column,'O')
        remark('Player 2\'s turn','darkred')
        dictonary(row,column,'O')

    else:
        output(row,column,'X')
        remark('Player 1\'s turn', 'darkgreen')
        dictonary(row, column, 'X')


    click_count += 1
    if click_count>8:
        remark('Game Over','Darkmagenta')



root = tk.Tk()
l = 220
h = 325
root.minsize(l,h)
root.maxsize(l,h)
root.title('Game')
root.iconbitmap('icon.ico')

titleL = tk.Label(root,text = "Tic-Tac-Toe",font = ('algerian',17),fg = 'chocolate')
titleL.grid(row = 0, column = 0, columnspan = 3, pady = 3)

creator = tk.Label(root,text = "Created By : E-Sor",font = ('harlow solid',15),fg = 'lightseagreen')
creator.grid(row = 1, column = 0, columnspan = 3)

buttons(4,0)
buttons(4,1)
buttons(4,2)

buttons(5,0)
buttons(5,1)
buttons(5,2)

buttons(6,0)
buttons(6,1)
buttons(6,2)



remark('Player 1\'s turn','darkgreen')
root.mainloop()