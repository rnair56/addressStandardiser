**To import the package**

``exec(compile(open("standardizeAddr.py", "rb").read(), "standardizeAddr.py", 'exec'))``

**Examples**

* Dictionary based abbrevation normalisation

Abbrv1 | Abbrv2
-------|--------
North | N
N    | North
     
      s1='6908 47TH HIGHWAY N'
      s2='6908 47TH HIGHWAY NORTH'
      s1,s2=standardizeAddr(s1,s2)
      6908 47TH HIGHWAY N   6908 47TH HIGHWAY N
     
      s1='6908 47TH HIGHWAY NORTH'
      s2='6908 47TH HIGHWAY N'
      s1,s2=standardizeAddr(s1,s2)
      6908 47TH HIGHWAY NORTH   6908 47TH HIGHWAY NORTH

* Combining
      
      s1='6908 47TH HIGHWAY N'
      s2='6908 47TH HIGH WAY N'
      s1,s2=standardizeAddr(s1,s2)
      6908 47TH HIGHWAY N   6908 47TH HIGHWAY N
      
* Filling in Qualified Address types

      QualifiedTypes=['LN','AVN']
      
      s1='6908 47TH HIGHWAY LN'
      s2='6908 47TH HIGHWAY'
      s1,s2=standardizeAddr(s1,s2)
      6908 47TH HIGHWAY LN  6908 47TH HIGHWAY LN

* Regular Expression bassed cleaning
  
  1. Removing special charachters 
  
         s1='6908 47TH HIGH-WAY'
         s2='6908 47TH HIGHWAY.'
         s1,s2=standardizeAddr(s1,s2)
         6908 47TH HIGHWAY LN  6908 47TH HIGHWAY LN
  
  2. String Formatting
  
         s1='12HUFFINGTON370'
         s2='12 HUFFINGTON 3116'
         s1,s2=standardizeAddr(s1,s2)
         12 HUFFINGTON 370  12 HUFFINGTON 3116
  
  3. Suffixes
         
             s1='6908 47TH LN N'
             s2='6908 47 WAY N'
             s1,s2=standardizeAddr(s1,s2)
             6908 47 LN N   6908 47 WAY N




