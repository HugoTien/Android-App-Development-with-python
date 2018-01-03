
# coding: utf-8

# In[1]:

import kivy
kivy.require('1.10.0')


# In[2]:

# 導入app
from kivy.app import App 


# In[3]:

# 從uix.label package導入Label
# "kivy.uix" 此package提供用户界面元素。
from kivy.uix.label import Label 


# In[4]:

class MyApp(App): # 建立類別
    
    def build(self): # build函数是要進行初始化和返回根控件的位置。
        return Label(text = 'Hello world') # label物件


# In[10]:

if __name__ == '__main__': 
    MyApp().run()          
    
# 無論什麼情況，app的入口都是用run()
# 這裡對MyApp這個class進行了初始化，並调用了這個類別的run()方法。


# In[5]:

# http://blog.konghy.cn/2017/04/24/python-entry-program/


# In[ ]:




# In[ ]:



