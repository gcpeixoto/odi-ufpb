# Builds directory tree for 'odi' project

import os

# --- TREE
# root dir
root = os.curdir

# parents folder
parents = ['misc','pkl','csv','xlsx']

# level 1 subfolder
xlsx_1 = ['no-class','the','qs']

# level 2 subfolder
xlsx_2 = ['staff','undergrads','grads']

# --- HELPERS        
p_namer = lambda x: f'Created parent directory \'{x}\'.'
c_namer = lambda x: f'Created child directory \'{x}\'.'
p_namer_ready = lambda x: f'Parent directory \'{x}\' already exists.'
c_namer_ready = lambda x: f'Child directory \'{x}\' already exists.'


# --- MAIN
def main():
    # builds parents
    for p in parents:
        p_name = os.path.join(root,p)

        try:        
            os.makedirs(p_name)
            print(p_namer(p_name))
        except FileExistsError:
            print(p_namer_ready(p_name))



    # builds level 1 subfolders
    for p in xlsx_1:    
        p_name = os.path.join(root,'xlsx',p)    

        try:        
            os.makedirs(p_name)
            print(c_namer(p_name))

        except FileExistsError:
            print(c_namer_ready(p_name))  


    # builds level 2 subfolders
    for p in xlsx_1:
        p_name = os.path.join(root,'xlsx',p)   

        for q in xlsx_2:
            q_name = os.path.join(p_name,q)

            try:        
                os.makedirs(q_name)
                print(c_namer(q_name))
            except FileExistsError:
                print(c_namer_ready(q_name))
                
if __name__ == '__main__':   
    main()