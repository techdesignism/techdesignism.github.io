#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

r = requests.get('https://techdesignism.com/sitemap')


# In[2]:


for x in r.text.split('\n'):
    if '?n=' in x:
        id = x.split('?n=')[1]
        rx = requests.get('https://techdesignism.com/?n='+id)
        soup = BeautifulSoup(rx.text, "lxml")
        title = (soup.title.text+' | Techdesignism')
        meta = soup.find_all('meta')
        for y in meta:
            if('property' in y.attrs):
                if(y.attrs['property'] == 'og:description'):
                    description = (y.attrs['content'])
                if(y.attrs['property'] == 'og:image'):
                    image = (y.attrs['content'])
        outhtml = (
f"""
<html>
<head>
<title>{title}</title>

<meta property="og:image" content="{image}" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />

</head>
<body>
<script>
window.location.href = "{x}";
</script>
{description}
</body>
</html>
""")
        with open(str(id)+'.html', 'w') as f:
            f.write(outhtml)


# In[3]:


sitemaptxt = ''
for x in r.text.split('\n'):
    if '?n=' in x:
        id = x.split('?n=')[1]
        sitemaptxt += (f"https://techdesignism.github.io/n/{id}.html\n")


# In[4]:


with open('sitemap.txt', 'w') as f:
    f.write(sitemaptxt)


# In[ ]:




