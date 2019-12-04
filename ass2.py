# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:29:31 2019

@author: Bharathi
"""




from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def login():
    return render_template('home.html')


@app.route('/Flask',  methods=['POST'])
def success():
# =============================================================================
#    if request.method == 'POST':
#        email = request.form['email']
#        abc = request.form['pass']
# =============================================================================
       return render_template('success.html')
# =============================================================================
#    else:
#        pass
# =============================================================================
if __name__ == '__main__':
    app.run(debug= False)