#Function to upgrade a pandas dataframe to any index.
def Power(Arr,index):
    Output_Arr=Arr
    for i in range(1,index):
        Output_Arr=Output_Arr*Arr
    return Output_Arr


# Recursive function to generate a combinations of numbers.
def generate_specific_combination(slots, possibilities, number):
    n = len(possibilities)
    combination = []
    
    for _ in range(slots):
        remainder = number % n
        combination.append(possibilities[remainder])
        number //= n
    
    combination.reverse()
    return combination
    
#Function to find out the common parts of a polynomial that matches a specific co-efficient. 
def common(a,b):
    c={}
    for key,value in a.items():
        split_key=key.split('*')
        split_b=b.split('*')
        IsCommon='Yes'
        for i in split_b:
            if i not in split_key:
                IsCommon='No'
                break
        if IsCommon=='Yes':
            for i in split_b:
                split_key.remove(i)
            if len(split_key)==0:
                c['integer']=value
            elif len(split_key)==1:
                c[split_key[0]]=value
            else:
                c['*'.join(split_key)]=value
    return c

#Function to merge two polynomials into a single polynomial.
def Merge(a, b):
    for key2 in b.keys():
        if key2 in a.keys():
            b[key2]=b[key2]+a[key2]
    return{**a,**b}

#Function to sort a co-efficient of a polynomial to its ascending order.
def sort(a):
    a=a.split("*")
    a.sort()
    return ('*'.join(a))


#Function to add two polynomials into a single polynomial.
def addition(a,b):
    for key1,value1 in a.items():
        sorted_key1=sort(key1)
        for key2,value2 in b.items():
            sorted_key2=sort(key2)
            if sorted_key1==sorted_key2:
                a[key1]=value1+value2
                del b[key2]
                break
    c={**a,**b}
    return c


#Function to subtract one polynomial from another.
def subtraction(a,b):
    for key2,value2 in b.items():
        b[key2]=(-1)*value2
    for key1,value1 in a.items():
        sorted_key1=sort(key1)
        for key2,value2 in b.items():
            sorted_key2=sort(key2)
            if sorted_key1==sorted_key2:
                a[key1]=value1+value2
                del b[key2]
                break
    c={**a,**b}
    return c


#Function to multiply two polynomials.
def multiplication(a,b):
    c={}
    index1=0
    index2=0
    index3=0
    for key1,value1 in a.items():
        for key2,value2 in b.items():
            if key1!="integer" and key2!="integer":
                key=key1+'*'+key2
                for key3,value3 in c.items():
                    if sort(key)==sort(key3):
                        if value3>pow(10,100):
                            value3=int(value3)
                        if value2>pow(10,100):
                            value2=int(value2)
                        if value1>pow(10,100):
                            value1=int(value1)                            
                        c[key3]=value3+value1*value2
                        index1=index1+1
                if index1==0:
                    if value2>pow(10,100):
                        value2=int(value2)
                    if value1>pow(10,100):
                        value1=int(value1)                            
                    c[sort(key)]=value1*value2
                index1=0
            elif key1=="integer" and key2!="integer":
                for key3,value3 in c.items():
                    if sort(key2)==sort(key3):
                        if value3>pow(10,100):
                            value3=int(value3)
                        if value2>pow(10,100):
                            value2=int(value2)
                        if value1>pow(10,100):
                            value1=int(value1)                            
                        c[key3]=value3+value1*value2
                        index2=index2+1
                if index2==0:
                    if value2>pow(10,100):
                        value2=int(value2)
                    if value1>pow(10,100):
                        value1=int(value1)
                    c[sort(key2)]=value1*value2                            
                index2=0
            elif key2=="integer" and key1!="integer":
                for key3,value3 in c.items():
                    if sort(key1)==sort(key3):
                        if value3>pow(10,100):
                            value3=int(value3)
                        if value2>pow(10,100):
                            value2=int(value2)
                        if value1>pow(10,100):
                            value1=int(value1)
                        c[key3]=value3+value1*value2
                        index3=index3+1
                if index3==0:
                    if value2>pow(10,100):
                        value2=int(value2)
                    if value1>pow(10,100):
                        value1=int(value1)
                    c[sort(key1)]=value1*value2
                index3=0
            else:
                if 'integer' in c.keys():
                    if value2>pow(10,100):
                        value2=int(value2)
                    if value1>pow(10,100):
                        value1=int(value1)
                    c['integer']==c['integer']+value1*value2
                else:
                    if value2>pow(10,100):
                        value2=int(value2)
                    if value1>pow(10,100):
                        value1=int(value1)
                    c['integer']=value1*value2
    return c


#Function to divide a polynomial with a number.
def division(a,b):
    for key,value in a.items():
        if b['integer']!= 0:
            a[key]=a[key]/b['integer']
    return a
    

#Function to find out the co-efficients a, b, c of a polynomial loss function J(w) = aw^2 + bw + c, in the form of functions.
def find_abc(J,w):
    abc=[]
    a={}
    b={}
    c={}
    for key,value in J.items():
        split_key=key.split('*')
        if split_key.count(w)==2:
            split_key.remove(w)
            split_key.remove(w)
            if len(split_key)==0:
                a['integer']=value
            else:
                a['*'.join(split_key)]=value
        elif split_key.count(w)==1:
            split_key.remove(w)
            if len(split_key)==0:
                b['integer']=value
            else:
                b['*'.join(split_key)]=value
        elif split_key.count(w)==0:
            c[key]=value
    abc.append(a)
    abc.append(b)
    abc.append(c)
    return abc
    
#Function to find out the co-efficients a, b, c of a polynomial loss function of the form J(w) = aw^2 + bw + c, in the form of numerical values
def find_abc_values(J,w,next_ws):

    abc=[]
    a=0
    b=0
    c=0

    for key,value in J.items():
        coefficient=key.split('*')
        index=coefficient.count(w)
        if index==0:
            pseudo_c=1
            for i in coefficient:
                if i!=w and i!='integer':
                  pseudo_c=pseudo_c*next_ws[i]
            pseudo_c=pseudo_c*value
            c=c+pseudo_c
        if index==1:
            pseudo_b=1
            for i in coefficient:
                if i!=w and i!='integer':
                  pseudo_b=pseudo_b*next_ws[i]
            pseudo_b=pseudo_b*value
            b=b+pseudo_b
        if index==2:
            pseudo_a=1
            for i in coefficient:
                if i!=w and i!='integer':
                  pseudo_a=pseudo_a*next_ws[i]
            pseudo_a=pseudo_a*value
            a=a+pseudo_a
            
    abc.append(a)
    abc.append(b)
    abc.append(c)
    return abc
    
#Function to build a polynomial loss function of the form J(w) = aw^2 + bw + c, as a string
def build_loss_function(abc,w):

    a=abc[0]
    b=abc[1]
    c=abc[2]
    loss_function=r'J('+w+')'+' = '+str(a)+'*'+w+'^2'+' + '+str(b)+'*'+w+' + '+str(c)
    
    return loss_function

#Function to find out the minimum value of a polynomial J = aw^2 + bw + c, and the specific value w where this minimum value occurs.
def find_JW(J,variable):
    JW=[]
    abc=find_abc(J,variable)
    b_sq=multiplication(abc[1],abc[1])
    a_into_4={}
    for key,value in abc[0].items():
        a_into_4[key]=value*4
    b_sq_by_4a=division(b_sq,a_into_4)
    J=subtraction(abc[2],b_sq_by_4a)
    minus_b={}
    for key,value in abc[1].items():
        minus_b[key]=value*(-1)
    a_into_2={}
    for key,value in abc[0].items():
        a_into_2[key]=value*2
    minus_b_by_2a=division(minus_b,a_into_2)
    w=minus_b_by_2a
    JW.append(J)
    JW.append(w)
    return JW
    
    
#Function to read data from a csv file.
def read_from_csv(csv_file):
    
    try:
        weights = {}
        powers={}

        with open(csv_file, mode='r') as file:
            lines = file.readlines()
        
            for line in lines[1:-1]:  
                row = line.strip().split(',') 
                weights[row[0]] = row[1]
                powers[row[0]]=row[2]
            
            bias=lines[-1].strip().split(',')[1]

        return [weights,powers,bias]
    except FileNotFoundError:
        print(f"Error: {csv_file} not found.")
        
#Function to plot loss functions with respect to the weight variables and bias.      
def plot_loss_functions(data,weights='all',feature_columns=None,label_column=None,model='linear',plot_range=[-2000, 2000, 100],save_plots=True):

    try:
    
        import numpy as np
        import matplotlib.pyplot as plt
    
        if feature_columns is None:
            feature_columns = list(range(len(data.columns) - 1))
        if label_column is None:
            label_column = len(data.columns) - 1
            
        l=len(feature_columns)
        
        if model=='linear':
            powers=[1 for i in range(0,l)]
        else:
            powers=model        
               
        Xs = [(feature_columns[i],powers[i]) for i in range(0,l)]
        Y=label_column
        J={}
        
        for i in range(0,len(Xs)):
            try:
                value = Power(data.iloc[:, Xs[i][0]], (Xs[i][1]) * 2).sum()
                J['w'+str(i+1)+'*'+'w'+str(i+1)] = value
            except OverflowError as e:
                value = Power(data.iloc[:, Xs[i][0]], (Xs[i][1]) * 2).sum()
                J['w'+str(i+1)+'*'+'w'+str(i+1)] = int(value)
            for j in range(i+1,len(Xs)):
                J['w'+str(i+1)+'*'+'w'+str(j+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*Power(data.iloc[:,Xs[j][0]],(Xs[j][1]))).sum())*2
            J['w'+str(i+1)+'*'+'b']=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))).sum())*2
            J['w'+str(i+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*data.iloc[:,Y]).sum())*(-2)
        J['b*b']=(data.iloc[:,Xs[0][0]]).count()
        J['b']=((data.iloc[:,Y]).sum())*(-2)
        J['integer']=Power((data.iloc[:,Y]),2).sum()

        Ws=[]
        J_min=J
        
        Js=[]
        loss_functions={}
        
        for i in range(0,len(Xs)):
            Js.append(J_min)
            JW=find_JW(J_min,'w'+str(i+1))
            W_min=JW[1]
            J_min=JW[0]
            Ws.append(W_min)
        loss_functions['b']=[J_min['b*b'],J_min['b'],J_min['integer']]
        Jb=find_JW(J_min,'b')
        b=Jb[1]['integer']
        J_min=Jb[0]['integer']
        
        if J_min<=0:
            print('Sorry. The model could not be formed due to overflow error.')
        else:    
            J_minimum=J_min

            Ws_and_b={}
            Ws_and_b['integer']=1
            Ws_and_b['b']=b
            
            for i in range(len(Ws)-1,-1,-1):
                abc=find_abc_values(Js[i],'w'+str(i+1),Ws_and_b)
                loss_functions['w'+str(i+1)]=abc
                Ws_and_b['w'+str(i+1)]=0
                for key,value in Ws[i].items():
                    Ws_and_b['w'+str(i+1)]=Ws_and_b['w'+str(i+1)]+Ws_and_b[key]*value
                       
            del Ws_and_b['integer']
            
            print('\n')
            print('Loss functions: ')
            
            if weights=='all':
                for key,value in loss_functions.items():
                    a=value[0]
                    b=value[1]
                    c=value[2]                   
                    l_function=build_loss_function(value,key)
                    print(l_function)
                    
                    w_values = np.linspace(plot_range[0],plot_range[1],plot_range[2])
                    J_values = a * w_values**2 + b * w_values + c
                    w_min = (-b/(2*a))
                    J_min = a * w_min**2 + b * w_min + c

                    plt.figure(figsize=(8, 6))
                    plt.plot(w_values, J_values, label=r'Weight Variable ('+key+')', color='blue', linewidth=1.5)

                    plt.scatter(w_min, J_min, color='#D2691E', label='Minimum Point', zorder=5)
                    plt.text(w_min + 200, J_min - 2000, f'({w_min:.6f}, {J_min:.6f})', color='#D2691E', fontsize=9)

                    plt.xlabel(r'Weight Variable ('+key+')', fontsize=10)
                    plt.ylabel(r'Loss Function ($J$)', fontsize=10)
                    plt.grid(visible=True, linestyle='--', alpha=0.7)
                    plt.legend(fontsize=9)
                    
                    plt.show()
                    
                    if save_plots==True:
                        plt.savefig(key+'.pdf', format='pdf', dpi=600, bbox_inches='tight')
            else:
                for key in weights:
                    value=loss_functions[key]
                    a=value[0]
                    b=value[1]
                    c=value[2]
                    
                    l_function=build_loss_function(value,key)
                    print(l_function)
                    
                    w_values = np.linspace(plot_range[0],plot_range[1],plot_range[2])
                    J_values = a * w_values**2 + b * w_values + c
                    w_min = (-b/(2*a))
                    J_min = a * w_min**2 + b * w_min + c

                    plt.figure(figsize=(8, 6))
                    plt.plot(w_values, J_values, label=r'Weight Variable ('+key+')', color='blue', linewidth=1.5)

                    plt.scatter(w_min, J_min, color='#D2691E', label='Minimum Point', zorder=5)
                    plt.text(w_min + 200, J_min - 2000, f'({w_min:.6f}, {J_min:.6f})', color='#D2691E', fontsize=9)

                    plt.xlabel(r'Weight Variable ('+key+')', fontsize=10)
                    plt.ylabel(r'Loss Function ($J$)', fontsize=10)
                    plt.grid(visible=True, linestyle='--', alpha=0.7)
                    plt.legend(fontsize=9)
                    
                    plt.show()
                    
                    if save_plots==True:
                        plt.savefig(key+'.pdf', format='pdf', dpi=600, bbox_inches='tight')             
            print('\n')
                       
    except ModuleNotFoundError:
        print("Module not found. Install numpy and matplotlib in your machine before accessing this function.")
        
#Function to compile a linear cms model.   
def compile_linear_model(data,feature_columns=None,label_column=None,print_loss=True,model_name='linear_cms_model',print_model=True,print_loss_functions=False):

    try:
    
        if feature_columns is None:
            feature_columns = list(range(len(data.columns) - 1))
        if label_column is None:
            label_column = len(data.columns) - 1
            
        l=len(feature_columns)
            
        powers=[1 for i in range(0,l)]            
               
        Xs = [(feature_columns[i],powers[i]) for i in range(0,l)]
        Y=label_column
        J={}
        
        for i in range(0,len(Xs)):
            try:
                value = Power(data.iloc[:, Xs[i][0]], (Xs[i][1]) * 2).sum()
                J['w'+str(i+1)+'*'+'w'+str(i+1)] = value
            except OverflowError as e:
                value = Power(data.iloc[:, Xs[i][0]], (Xs[i][1]) * 2).sum()
                J['w'+str(i+1)+'*'+'w'+str(i+1)] = int(value)
            for j in range(i+1,len(Xs)):
                J['w'+str(i+1)+'*'+'w'+str(j+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*Power(data.iloc[:,Xs[j][0]],(Xs[j][1]))).sum())*2
            J['w'+str(i+1)+'*'+'b']=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))).sum())*2
            J['w'+str(i+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*data.iloc[:,Y]).sum())*(-2)
        J['b*b']=(data.iloc[:,Xs[0][0]]).count()
        J['b']=((data.iloc[:,Y]).sum())*(-2)
        J['integer']=Power((data.iloc[:,Y]),2).sum()

        Ws=[]
        J_min=J
        
        Js=[]
        loss_functions=[]
        
        for i in range(0,len(Xs)):
            Js.append(J_min)
            JW=find_JW(J_min,'w'+str(i+1))
            W_min=JW[1]
            J_min=JW[0]
            Ws.append(W_min)
        loss_functions.append(build_loss_function([J_min['b*b'],J_min['b'],J_min['integer']],'b'))
        Jb=find_JW(J_min,'b')
        b=Jb[1]['integer']
        J_min=Jb[0]['integer']
        
        if J_min<=0:
            print('Sorry. The model could not be formed due to overflow error.')
        else:    
            J_minimum=J_min
            Ws_and_b={}
            Ws_and_b['integer']=1
            Ws_and_b['b']=b
            
            for i in range(len(Ws)-1,-1,-1):
                abc=find_abc_values(Js[i],'w'+str(i+1),Ws_and_b)
                loss_functions.append(build_loss_function(abc,'w'+str(i+1)))
                Ws_and_b['w'+str(i+1)]=0
                for key,value in Ws[i].items():
                    Ws_and_b['w'+str(i+1)]=Ws_and_b['w'+str(i+1)]+Ws_and_b[key]*value
                       
            del Ws_and_b['integer']
            
            list_model=[]
            list_model.append(['feature','weight','power'])
            index=1
            for i in feature_columns:
                list_model.append([data.columns[i],Ws_and_b['w'+str(index)],powers[index-1]])
                index=index+1
            list_model.append(['bias',Ws_and_b['b'],'---'])
            
            if print_loss_functions==True:
                print('\n')
                print('Loss functions: ')
                for l_function in loss_functions:
                    print(l_function)
                print('\n')
                
            if print_model==True:        
                print('\n')
                col_widths = [max(len(str(item)) for item in col) for col in zip(*list_model)]
                for row in list_model:
                    print(" | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))
                    
            if print_loss==True:
                print('\n')
                print('Total loss: '+str(J_minimum))

            with open(model_name+'.csv', mode='w', newline='') as file:
                for row in list_model:
                    file.write(','.join(map(str, row)) + '\n')

            print('\n')
            print('Successfully saved the weights and bias in '+model_name+'.csv.')
            
        
    except PermissionError as e:
        print('PermissionError: There is possibly a file opened with the name '+saved_model_name+'.csv. Close it and try again, or try with a different name.')
    
            
#Function to compile a custom cms model with a specific combination of powers.   
def compile_custom_model(data,powers=None,feature_columns=None,label_column=None,print_loss=True,model_name='custom_cms_model',print_model=True,print_loss_functions=False):

    try:
    
        if feature_columns is None:
            feature_columns = list(range(len(data.columns) - 1)) 
        if label_column is None:
            label_column = len(data.columns) - 1
            
        l=len(feature_columns)
            
        if powers is None:
            powers=[1 for i in range(0,l)]            
               
        Xs = [(feature_columns[i],powers[i]) for i in range(0,l)]
        Y=label_column
        J={}
        
        for i in range(0,len(Xs)):
            try:
                value = Power(data.iloc[:, Xs[i][0]], (Xs[i][1]) * 2).sum()
                J['w'+str(i+1)+'*'+'w'+str(i+1)] = value
            except OverflowError as e:
                value = Power(data.iloc[:, Xs[i][0]], (Xs[i][1]) * 2).sum()
                J['w'+str(i+1)+'*'+'w'+str(i+1)] = int(value)
            for j in range(i+1,len(Xs)):
                J['w'+str(i+1)+'*'+'w'+str(j+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*Power(data.iloc[:,Xs[j][0]],(Xs[j][1]))).sum())*2
            J['w'+str(i+1)+'*'+'b']=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))).sum())*2
            J['w'+str(i+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*data.iloc[:,Y]).sum())*(-2)
        J['b*b']=(data.iloc[:,Xs[0][0]]).count()
        J['b']=((data.iloc[:,Y]).sum())*(-2)
        J['integer']=Power((data.iloc[:,Y]),2).sum()

        Ws=[]
        J_min=J
        
        Js=[]
        loss_functions=[]
        
        for i in range(0,len(Xs)):
            Js.append(J_min)
            JW=find_JW(J_min,'w'+str(i+1))
            W_min=JW[1]
            J_min=JW[0]
            Ws.append(W_min)
        loss_functions.append(build_loss_function([J_min['b*b'],J_min['b'],J_min['integer']],'b'))
        Jb=find_JW(J_min,'b')
        b=Jb[1]['integer']
        J_min=Jb[0]['integer']
        
        if J_min<=0:
            print('Sorry. The model could not be formed due to overflow error.')
        else:    
            J_minimum=J_min

            Ws_and_b={}
            Ws_and_b['integer']=1
            Ws_and_b['b']=b
            
            for i in range(len(Ws)-1,-1,-1):
                abc=find_abc_values(Js[i],'w'+str(i+1),Ws_and_b)
                loss_functions.append(build_loss_function(abc,'w'+str(i+1)))
                Ws_and_b['w'+str(i+1)]=0
                for key,value in Ws[i].items():
                    Ws_and_b['w'+str(i+1)]=Ws_and_b['w'+str(i+1)]+Ws_and_b[key]*value
                       
            del Ws_and_b['integer']
            
            list_model=[]
            list_model.append(['feature','weight','power'])
            index=1
            for i in feature_columns:
                list_model.append([data.columns[i],Ws_and_b['w'+str(index)],powers[index-1]])
                index=index+1
            list_model.append(['bias',Ws_and_b['b'],'---'])
            
            if print_loss_functions==True:
                print('\n')
                print('Loss functions: ')
                for l_function in loss_functions:
                    print(l_function)
                print('\n')
                
            if print_model==True:        
                print('\n')
                col_widths = [max(len(str(item)) for item in col) for col in zip(*list_model)]
                for row in list_model:
                    print(" | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))
                    
            if print_loss==True:
                print('\n')
                print('Total loss: '+str(J_minimum))

            with open(model_name+'.csv', mode='w', newline='') as file:
                for row in list_model:
                    file.write(','.join(map(str, row)) + '\n')

            print('\n')
            print('Successfully saved the weights and bias in '+model_name+'.csv.')
            
        
    except PermissionError as e:
        print('PermissionError: There is possibly a file opened with the name '+saved_model_name+'.csv. Close it and try again, or try with a different name.')


#Function to compile the best cms model from all the possible combinations, upto a pre-defined maximum power.
def compile_best_model(data,max_power=1,feature_columns=None,label_column=None,print_loss=True,print_best_model=True,best_model_name='best_cms_model',save_first_model=True,first_model_name='first_cms_model'):

    try:
    
        if feature_columns is None:
            feature_columns = list(range(len(data.columns) - 1))  
        if label_column is None:
            label_column = len(data.columns) - 1
        
        possibilities=[i for i in range(1,max_power+1)]
        l=len(feature_columns)

        combination = generate_specific_combination(l, possibilities, 0)
        print('Combination: '+str(combination))
        
        Xs = [(feature_columns[i],combination[i]) for i in range(0,l)]
        Y=label_column
        J={}
        
        for i in range(0,len(Xs)):
            J['w'+str(i+1)+'*'+'w'+str(i+1)]=(Power(data.iloc[:,Xs[i][0]],(Xs[i][1])*2)).sum()
            for j in range(i+1,len(Xs)):
                J['w'+str(i+1)+'*'+'w'+str(j+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*Power(data.iloc[:,Xs[j][0]],(Xs[j][1]))).sum())*2
            J['w'+str(i+1)+'*'+'b']=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))).sum())*2
            J['w'+str(i+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*data.iloc[:,Y]).sum())*(-2)
        J['b*b']=(data.iloc[:,Xs[0][0]]).count()
        J['b']=((data.iloc[:,Y]).sum())*(-2)
        J['integer']=Power((data.iloc[:,Y]),2).sum()

        Ws=[]
        J_min=J
        for i in range(0,len(Xs)):
            JW=find_JW(J_min,'w'+str(i+1))
            W_min=JW[1]
            J_min=JW[0]
            Ws.append(W_min)
        Jb=find_JW(J_min,'b')
        b=Jb[1]['integer']
        J_min=Jb[0]['integer']
        
        J_minimum=0
        
        model_formed=False
        
        if J_min<=0:
            print('Model '+str(combination)+' could not be formed due to overflow error.')
        else:
            model_formed=True
            if print_loss==True:
                print('loss: '+str(J_min))
                print('\n')
            
            J_minimum=J_min

            Ws_and_b={}
            Ws_and_b['integer']=1
            Ws_and_b['b']=b
            for i in range(len(Ws)-1,-1,-1):
                Ws_and_b['w'+str(i+1)]=0
                for key,value in Ws[i].items():
                    Ws_and_b['w'+str(i+1)]=Ws_and_b['w'+str(i+1)]+Ws_and_b[key]*value
            final_combination=combination
            
            del Ws_and_b['integer']
            
            if save_first_model==True:
                list_model=[]
                list_model.append(['feature','weight','power'])
                index=1
                for i in feature_columns:
                    list_model.append([data.columns[i],Ws_and_b['w'+str(index)],final_combination[index-1]])
                    index=index+1
                list_model.append(['bias',Ws_and_b['b'],'---'])

                with open(first_model_name+'.csv', mode='w', newline='') as file:
                    for row in list_model:
                        file.write(','.join(map(str, row)) + '\n')

        for list_number in range(1,Power(max_power,l)):
        
            combination = generate_specific_combination(l, possibilities, list_number)
            print('Combination: '+str(combination))
            Xs = [(feature_columns[i],combination[i]) for i in range(0,l)]
            Y=label_column
            J={}
            
            for i in range(0,len(Xs)):
                J['w'+str(i+1)+'*'+'w'+str(i+1)]=(Power(data.iloc[:,Xs[i][0]],(Xs[i][1])*2)).sum()
                for j in range(i+1,len(Xs)):
                    J['w'+str(i+1)+'*'+'w'+str(j+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*Power(data.iloc[:,Xs[j][0]],(Xs[j][1]))).sum())*2
                J['w'+str(i+1)+'*'+'b']=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))).sum())*2
                J['w'+str(i+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*data.iloc[:,Y]).sum())*(-2)
            J['b*b']=(data.iloc[:,Xs[0][0]]).count()
            J['b']=((data.iloc[:,Y]).sum())*(-2)
            J['integer']=Power((data.iloc[:,Y]),2).sum()

            Ws=[]
            J_min=J
            for i in range(0,len(Xs)):
                JW=find_JW(J_min,'w'+str(i+1))
                W_min=JW[1]
                J_min=JW[0]
                Ws.append(W_min)
            Jb=find_JW(J_min,'b')
            b=Jb[1]['integer']
            J_min=Jb[0]['integer']
            
            if J_min<=0:
                print('Model '+str(combination)+' could not be formed due to overflow error.')
            else:
                model_formed=True
                if print_loss==True:
                    print('loss: '+str(J_min))
                    print('\n')
                
                if J_min<J_minimum:
                    
                    Ws_and_b={}
                    Ws_and_b['integer']=1
                    Ws_and_b['b']=b
                    for i in range(len(Ws)-1,-1,-1):
                        Ws_and_b['w'+str(i+1)]=0
                        for key,value in Ws[i].items():
                            Ws_and_b['w'+str(i+1)]=Ws_and_b['w'+str(i+1)]+Ws_and_b[key]*value                           
                    
                    final_combination=combination
                    J_minimum=J_min

                    del Ws_and_b['integer']
                    
        if model_formed==True:
            list_model=[]
            list_model.append(['feature','weight','power'])
            index=1
            for i in feature_columns:
                list_model.append([data.columns[i],Ws_and_b['w'+str(index)],final_combination[index-1]])
                index=index+1
            list_model.append(['bias',Ws_and_b['b'],'---'])

            if print_best_model==True:
                print('\n')
                col_widths = [max(len(str(item)) for item in col) for col in zip(*list_model)]
                for row in list_model:
                    print(" | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))

            if print_loss==True:
                print('\n')
                print('Total loss: '+str(J_minimum))

            with open(best_model_name+'.csv', mode='w', newline='') as file:
                for row in list_model:
                    file.write(','.join(map(str, row)) + '\n')
            print('\n')
            print('Successfully saved the weights and bias in '+best_model_name+'.csv.')
        
    except PermissionError as e:
        print('PermissionError: There is possibly a file opened with the name '+saved_model_name+'.csv. Close it and try again, or try with a different name.')


#Function to compile all cms models of all the possible combinations, upto a pre-defined maximum power.
def compile_all_models(data,max_power=1,feature_columns=None,label_column=None,print_loss=True,print_model=True,model_name='cms_model'):

    try:
    
        if feature_columns is None:
            feature_columns = list(range(len(data.columns) - 1)) 
        if label_column is None:
            label_column = len(data.columns) - 1
        
        possibilities=[i for i in range(1,max_power+1)]
        l=len(feature_columns)

        for list_number in range(0,Power(max_power,l)):
        
            combination = generate_specific_combination(l, possibilities, list_number)
            print('Combination: '+str(combination))
            Xs = [(feature_columns[i],combination[i]) for i in range(0,l)]
            Y=label_column
            J={}
            
            for i in range(0,len(Xs)):
                J['w'+str(i+1)+'*'+'w'+str(i+1)]=(Power(data.iloc[:,Xs[i][0]],(Xs[i][1])*2)).sum()
                for j in range(i+1,len(Xs)):
                    J['w'+str(i+1)+'*'+'w'+str(j+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*Power(data.iloc[:,Xs[j][0]],(Xs[j][1]))).sum())*2
                J['w'+str(i+1)+'*'+'b']=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))).sum())*2
                J['w'+str(i+1)]=((Power(data.iloc[:,Xs[i][0]],(Xs[i][1]))*data.iloc[:,Y]).sum())*(-2)
            J['b*b']=(data.iloc[:,Xs[0][0]]).count()
            J['b']=((data.iloc[:,Y]).sum())*(-2)
            J['integer']=Power((data.iloc[:,Y]),2).sum()

            Ws=[]
            J_min=J
            for i in range(0,len(Xs)):
                JW=find_JW(J_min,'w'+str(i+1))
                W_min=JW[1]
                J_min=JW[0]
                Ws.append(W_min)
            Jb=find_JW(J_min,'b')
            b=Jb[1]['integer']
            J_min=Jb[0]['integer']
            
            if J_min<=0:
                print('Model '+str(combination)+' could not be formed due to overflow error.')
            else:
                if print_loss==True:
                    print('loss: '+str(J_min))
                    print('\n')
                    
                Ws_and_b={}
                Ws_and_b['integer']=1
                Ws_and_b['b']=b
                for i in range(len(Ws)-1,-1,-1):
                    Ws_and_b['w'+str(i+1)]=0
                    for key,value in Ws[i].items():
                        Ws_and_b['w'+str(i+1)]=Ws_and_b['w'+str(i+1)]+Ws_and_b[key]*value                           

                del Ws_and_b['integer']
                    
                list_model=[]
                list_model.append(['feature','weight','power'])
                index=1
                for i in feature_columns:
                    list_model.append([data.columns[i],Ws_and_b['w'+str(index)],combination[index-1]])
                    index=index+1
                list_model.append(['bias',Ws_and_b['b'],'---'])

                if print_model==True:
                    print('\n')
                    col_widths = [max(len(str(item)) for item in col) for col in zip(*list_model)]
                    for row in list_model:
                        print(" | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))

                with open(model_name+'_'+str(list_number+1)+'.csv', mode='w', newline='') as file:
                    for row in list_model:
                        file.write(','.join(map(str, row)) + '\n')
                print('\n')
                print('Successfully saved the weights and bias in '+model_name+'_'+str(list_number+1)+'.csv')
                print('\n')
        
    except PermissionError as e:
        print('PermissionError: There is possibly a file opened with the name '+model_name+'_'+str(list_number+1)+'.csv. Close it and try again, or try with a different name.')


#Function to generate output of a pandas dataframe according to a given cms model.
def predict(data,load_model,print_output=True,save_output_file=True,saved_file_name='predicted cms file'):
    
    try:
        info=read_from_csv(load_model)

        weights=info[0]
        powers=info[1]
        bias=info[2]

        if isinstance(data, list):
            weights_list = list(weights.values())
            powers_list = list(powers.values())
            print('Number of features provided: '+str(len(data)))
            print('Total number of weights: '+str(len(weights_list)))
            predicted_value=0
            if len(data)<len(weights_list):
                end=len(data)
            elif len(data)>len(weights_list):
                end=len(weights_list)
            else:
                end=len(weights_list)
            for i in range(0,end):
                predicted_value=predicted_value+float(weights_list[i])*Power(data[i],int(powers_list[i]))
            predicted_value=predicted_value+float(bias)
            print('\n')
            print('Predicted value for the provided data: '+str(predicted_value))
        else:
            data['predicted_value']=0
            for column in data.columns[:-1]:
                if column in weights:
                    if column in powers:
                        data['predicted_value']=data['predicted_value']+float(weights[column])*(Power(data[column],int(powers[column])))
                    else:
                        print('There is no predicted power for '+column+'.')
                else:
                    print('There is no predicted weight for '+column+'.')
            data['predicted_value']=data['predicted_value']+float(bias)
            if print_output==True:
                print(data['predicted_value'])
            if save_output_file==True:
                data.to_csv(saved_file_name+'.csv', index=False)
                print('Predicted data saved in '+saved_file_name+'.csv.')
                
    except PermissionError as e:
        print('PermissionError: There is possibly a file opened with the name '+saved_file_name+'.csv. Close it and try again, or try with a different name.')



#Experimenting with real-world dataset.
import pandas as pd

data=pd.read_csv('dataset.csv')

plot_loss_functions(data,weights='all',save_plots=False) #displays and plots the loss functions.

compile_linear_model(data=data) #compiles the best-fit linear model and displays the coefficients.
