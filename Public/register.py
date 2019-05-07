from flask import Flask, request
from blockchain import createwallet
import json
app = Flask(__name__)

@app.route('/register', methods=['GET'])
def register():
    wallet = createwallet.create_wallet('1234password', '58ck39ajuiw', 'http://localhost:5000', label = 'Test wallet',email='devod0485@gmail.com')
    print(wallet)
if __name__ == '__main__':
   app.run(debug=True)