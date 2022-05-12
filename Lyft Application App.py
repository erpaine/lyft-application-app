from __future__ import absolute_import
from flask import Flask, request
import json

app = Flask(__name__)
@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        value = request.form.get('string_to_cut')
    
        return_string = ''
        for elem in value[2: :3]:
            return_string = return_string + elem

        new_dict = {
            "return_string": return_string
        }

        return json.dumps(new_dict)
    
    else: 
        
        return '''
            <form method="POST">
                <div><label>String to Cut: <input type="text" name="string_to_cut"></label></div>
                <input type="submit" value="Submit">
            </form>'''