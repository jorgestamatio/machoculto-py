#!/usr/bin/env python
# -*- coding: UTF-8 -*-

## enable debugging
import cgitb
cgitb.enable()

#import cgi for processing the post requests
import cgi
form = cgi.FieldStorage()

#get the username post, if none is set, use "world"
user = form.getfirst('username','world')

#Print everything
print """\
Content-Type: text/html;charset=utf-8\n
<html>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'>
<title>Hello Python!</title>
<style>
.form{{
width: 15%;
min-width: 180px;
margin: 100px auto 0 auto;
padding: 2%;
border: 1px solid #f0f0f0;
text-align: center;
}}
.form input{{
box-shadow: none;
border: 1px solid #f0f0f0;
padding: 8px 2%;
background: #f5f5f5;
margin: 5px auto !important;
width: 96%;
}}
.form input[type='submit']{{
width: 96%;
}}
.form input[type='submit']:hover{{
cursor: pointer;
background-color: #f0f0f0;
}}
</style>
<body>
  <div class='form'>
    <h1>Hello, {0}!</h1>
    <form action='http://jstamatio.com/cgi-bin/machoculto-py/index.py' method='POST'>
      <input type='text' name='username' placeholder='My name is ...'>
      <input type='submit' value='Say my name, Macho!'>
    </form>
  </div>
</body>
</html>
""".format(user)