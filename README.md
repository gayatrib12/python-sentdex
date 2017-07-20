# pythonSentDex

#set-up issues for Python - 
#FYI - Python v2.7

#Environment requirements - 
  1. Clean layout for coding
  2. Support for Git clone/commit/push from within IDE itself
  3. Easy install of Python packages.
  
#Options - 
  1. Visual Studio Community 2015
    Pros:- 
    - Made use of before
    - Great IDE with support for Git clone/commit/push
    
    Cons:-
    - No clarity regarding creation of Virtual environment.
    
  2. Anaconda - Spyder
    Pros:-
    - Better support from community.
    - Seems to be preferred IDE
    
    Cons:-
    - No clarity regarding use, setup
    
    
#Steps followed - 
1. Visual Studio Community 2015

  a)Issue - Failed to install Numpy packages
    Solution - Install Microsoft Visual C++ Compiler
    
  b)Issue - On visual studio, no matching distribution found for PIL PIL failed to install 
    Solution - Currently using Python v2.7, and although PIL is preferred version for it, try installing Pillow through cmd window first and then try installing through Visual Studio 2015.
                
  c)Issue - Can't find a usable init.tcl in the following directories windows     
  Solution - Copy the contents of C:\Python27\tcl into C:\Python27\Lib.
  
  d)Issue - ValueError: assignment destination is read-only
  Solution - using np.array() instead of np.asarray() solved the problem
  As per https://philbull.wordpress.com/2013/06/27/making-numpy-arrays-read-only/
  
  e)
  
