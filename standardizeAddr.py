fillers=['AVE','APT','STREET','RD','ROAD']
pairs={'WEST':'W',
       'EAST':'E',
       'SOUTH':'S',
       'NORTH':'N',
       'W':'WEST',
       'N':'NORTH',
       'S':'SOUTH',
       'E':'EAST',
       'STREET':'ST',
       'ST':['STREET','AVE','STREER','STREE','STEET'],
       'ROAD':'RD',
       'RD':'ROAD',
       'STREER':'ST',
       'STREE':'ST',
       'AVENUE':['AVE','AVN'],
       'AVE':['AVENUE','AVN','ST'],
       'TERRACE':'TER',
       'TER':'TERRACE',
       'AVN':['AVE','AVENUE'],
       'VIEW':'VW',
       'VW':'VIEW',
       'HWY':'HIGHWAY',
       'HIGHWAY':'HWY',
       'LANE':'LN',
       'LN':'LANE'}
##{key:[to_replace,replacement_value]}
replacements={
            'WEST': ['WEST','W'],
            'EAST':['EAST','E'],
            'SOUTH':['SOUTH','S'],
            'NORTH':['NORTH','N'],
            'W':['W','WEST'],
            'N':['N','NORTH'],
            'S':['S','SOUTH'],
            'E':['E','EAST'],
            'STREET':['STREET','ST'],
            'ST':[['ST','STREET'],['ST','AVE'],['ST','STREER'],['ST','STREE'],['ST','STEET']],
            'ROAD':['ROAD','RD'],
            'RD':['RD','ROAD'],
            'STREER':['STREER','ST'],
            'STREE':['STREE','ST'],
            'AVENUE':[['AVENUE','AVE'],['AVENUE','AVN']],
            'AVE':[['AVE','AVENUE'],['AVE','AVN'],['AVE','ST']],
            'TERRACE':['TERRACE','TER'],
            'TER':['TER','TERRACE'],
            'AVN':[['AVN','AVE'],['AVN','AVENUE']],
            'VIEW':['VIEW','VW'],
            'VW':['VW','VIEW'],
            'HWY':['HWY','HIGHWAY'],
            'HIGHWAY':['HIGHWAY','HWY'],
            'LANE':['LANE','LN'],
            'LN':['LN','LANE']

    }

import re

def normaliser(s1,s2):
    '''s2_n is run over regular expressions to normalise'''
    s1=str(s1).upper().strip()
    s2=str(s2).upper().strip()
    s1_n=regexmod(s1)
    s2_n=regexmod(s2)
    '''replace No suffixes th,rd and nd if its present in one addres and not in other'''
    if re.search(r'\b([\d]+)(TH|RD|ND|ST)\b',s1_n):
        if not re.search(r'\b([\d]+)(TH|RD|ND|ST)\b',s2_n):
            s1_n=re.sub(r'\b([\d]+)(TH|RD|ND|ST)\b',r'\1',s1_n,1)
    elif re.search(r'\b([\d]+)(TH|RD|ND|ST)\b',s2_n):
        s2_n=re.sub(r'\b([\d]+)(TH|RD|ND|ST)\b',r'\1',s2_n,1)
    
    #s1_n=re.sub(r'(^[\d]+)([a-zA-Z]+) ([\d]+)([a-zA-Z]+)',r'\1 \2 \3 \4',s1)
    #s2_n=re.sub(r'(^[\d]+)([a-zA-Z]+) ([\d]+)([a-zA-Z]+)',r'\1 \2 \3 \4',s2)
    
    s1_n_l=s1_n.split()
    s2_n_l=s2_n.split()
    #pdb.set_trace()
    ##are the differences abbrevations
    set_1_m_2=set(s1_n_l)-set(s2_n_l)
    set_2_m_1=set(s2_n_l)-set(s1_n_l)
    s1_n_update=s1_n
    if(set_1_m_2):
        
        for i in set_1_m_2:
            try:
                #print(i)
                if isinstance(pairs[i],list):
                    cnt=len(pairs[i])
                elif isinstance(pairs[i],str):
                    cnt=1
                else:
                    sys.exit("aa! errors!")
                if cnt>1:
                    
                    while cnt>0:
                        
                        if(pairs[i][cnt-1] in set_2_m_1):
                            #print(cnt)
                            #print('run replacement for ', i, replacements[i][cnt-1][i])
                            #print(replacements[i][cnt-1])
                            #s1_n_update=re.sub(replacements[i][0],replacements[i][1],s1_n_update)
                            words=['re.sub(','r','\'\\b',replacements[i][cnt-1][0],'\\b\'',',','\'',replacements[i][cnt-1][1],'\'',',','\'',s1_n_update,'\'',')']
            
                            s1_n_update=eval("".join(words))
                        cnt-=1
                elif cnt==1:
                    if(pairs[i] in set_2_m_1):
                        #print(cnt)
                        #print('run replacement for ', i, replacements[i][cnt-1][i])
                        #print(replacements[i][cnt-1])
                        #s1_n_update=re.sub(replacements[i][0],replacements[i][1],s1_n_update)
                        words=['re.sub(','r','\'\\b',replacements[i][0],'\\b\'',',','\'',replacements[i][1],'\'',',','\'',s1_n_update,'\'',')']
                
                        s1_n_update=eval("".join(words))
            
            except KeyError:
                continue
        
    
    return([s1_n_update,s2_n])
    
    
def regexmod(s):
    #import re
    s=re.sub(r'[^a-zA-Z0-9 ]','',s)
    s=re.sub(r'(^[\d]+)([a-zA-Z]+)([\d]+)([a-zA-Z]+)',r'\1\2 \3\4',s)
    s=re.sub(r'(^[\d]+)([a-zA-Z]+) ([\d]+)([a-zA-Z]{4,})',r'\1\2 \3 \4',s)
    s=re.sub(r'(^[\d]+)([a-zA-Z]+) ([\d]+)([a-zA-Z]{4,})',r'\1\2 \3 \4',s)
    s=re.sub(r'(^[\d]+) ([\d]+)([a-zA-Z]{4,})',r'\1 \2 \3',s)
    #s=re.sub(r'(^[\d]+)(ND-RD-TH) ([A-Za-z0-9 ].*)',r'\1 \3',s)
    #s=re.sub(r'\b([\d]+)(TH|RD|ND)\b',r'\1',s,1)##not added ST as IT OCCURS INTERCHANGED WITH STREET, only replaces the first occurance
    
    return(s)
#s1_n='2347 NW CANN ON AVE'
#s2_n='2347 CANNON AVE'

def combine(s1,s2):
    
    s1_n_l=s1.split()
    s2_n_l=s2.split()
    #pdb.set_trace()
    ##are the differences abbrevations
    set_1_m_2=set(s1_n_l)-set(s2_n_l)
    set_2_m_1=set(s2_n_l)-set(s1_n_l)
    l1=list(set_1_m_2)
    l2=list(set_2_m_1)
    #print(set_1_m_2)
    #print(set_2_m_1)
    flag=False
    if len(l1)>1:
        if(not flag):
            for pos,ele in enumerate(l1):
                if(pos<len(l1)):
                    for j in range(pos+1,len(l1)):
                        nw1="".join([ele,l1[j]])
                        nw2="".join([l1[j],ele])
                        if nw1 in l2:
                            words=['re.sub(','r','\'\\b',ele,'\\b\'',',','\'',nw1,'\'',',','\'',s1,'\'',')']
                            s1_new=eval("".join(words))
                            words=['re.sub(','r','\'\\b',l1[j],' \\b\'',',','\'\'',',','\'',s1_new,'\'',')']
                            s1_new=eval("".join(words))
                            flag=True
                            return([s1_new,s2])
                        elif nw2 in l2:
                            words=['re.sub(','r','\'\\b',ele,'\\b\'',',','\'',nw2,'\'',',','\'',s1,'\'',')']
                            s1_new=eval("".join(words))
                            words=['re.sub(','r','\'\\b',l1[j],' \\b\'',',','\'\'',',','\'',s1_new,'\'',')']
                            s1_new=eval("".join(words))
                            flag=True
                            return([s1_new,s2])
        if(not flag):
            for pos,ele in enumerate(l2):
                if(pos<len(l2)):
                    for j in range(pos+1,len(l2)):
                        nw1="".join([ele,l2[j]])
                        nw2="".join([l2[j],ele])
                        if nw1 in l1:
                            words=['re.sub(','r','\'\\b',ele,'\\b\'',',','\'',nw1,'\'',',','\'',s2,'\'',')']
                            s2_new=eval("".join(words))
                            words=['re.sub(','r','\'\\b',l2[j],' \\b\'',',','\'\'',',','\'',s2_new,'\'',')']
                            s2_new=eval("".join(words))
                            flag=True
                            return([s1,s2_new])
                        elif nw2 in l1:
                            words=['re.sub(','r','\'\\b',ele,'\\b\'',',','\'',nw2,'\'',',','\'',s2,'\'',')']
                            s2_new=eval("".join(words))
                            words=['re.sub(','r','\'\\b',l2[j],' \\b\'',',','\'\'',',','\'',s2_new,'\'',')']
                            s2_new=eval("".join(words))
                            flag=True
                            return([s1,s2_new])
    elif len(l2)>1:
        if(not flag):
            for pos,ele in enumerate(l2):
                if(pos<len(l2)):
                    for j in range(pos+1,len(l2)):
                        nw1="".join([ele,l2[j]])
                        nw2="".join([l2[j],ele])
                        if nw1 in l1:
                            words=['re.sub(','r','\'\\b',ele,'\\b\'',',','\'',nw1,'\'',',','\'',s2,'\'',')']
                            s2_new=eval("".join(words))
                            words=['re.sub(','r','\'\\b',l2[j],' \\b\'',',','\'\'',',','\'',s2_new,'\'',')']
                            s2_new=eval("".join(words))
                            flag=True
                            return([s1,s2_new])
                        elif nw2 in l1:
                            words=['re.sub(','r','\'\\b',ele,'\\b\'',',','\'',nw2,'\'',',','\'',s2,'\'',')']
                            s2_new=eval("".join(words))
                            words=['re.sub(','r','\'\\b',l2[j],' \\b\'',',','\'\'',',','\'',s2_new,'\'',')']
                            s2_new=eval("".join(words))
                            flag=True
                            return([s1,s2_new])
    
    return([s1,s2])
                        
                
def filler(s1,s2,fillers=fillers):
    s1=str(s1).upper().strip()
    s2=str(s2).upper().strip()
    
    s1_n=regexmod(s1)
    s2_n=regexmod(s2)
    
    s1_n_l=s1_n.split()
    s2_n_l=s2_n.split()
    
    set_1_m_2=set(s1_n_l)-set(s2_n_l)
    set_2_m_1=set(s2_n_l)-set(s1_n_l)

    flag=False
    if not flag:
        for i in set_1_m_2:
            if i in fillers:
                s2_n=s2+' '+i##just appending string to the end; sorting should take care of position
                             ##theres probably a better way to do this!! Look at the string in pos n-1 and
                            ##update at that position
                flag=True

                break
    if not flag:
        for i in set_2_m_1:
            if i in fillers:
                s1_n=s1+' '+i
                flag=True
             
                break
    return([s1_n,s2_n])
    
                   
    
def standardizeAddr(s1,s2):
    s1,s2=normaliser(s1,s2)
    #print(s1)
    #print(s2)
    s1,s2=combine(s1,s2)
    return(filler(s1,s2))    
##if __name__== "main":
#	 standardizeAddr(s1,s2)
