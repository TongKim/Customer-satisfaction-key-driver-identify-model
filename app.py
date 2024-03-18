#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
from simulator import satisfaction_simulator, coefficients

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        improvements = {}
        for feature in coefficients['Feature']:
            improvement = float(request.form.get(feature, 0))
            if improvement != 0:
                improvements[feature] = improvement
        impact_percentage = satisfaction_simulator(improvements)
        return render_template('index.html', impact_percentage=impact_percentage, coefficients=coefficients)
    return render_template('index.html', coefficients=coefficients)

if __name__ == '__main__':
    app.run(debug=True, port=0)

# In[ ]:




