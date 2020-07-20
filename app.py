from flask import Flask
from process_site import fetchTotalData,fetchStatewiseData

app = Flask(__name__)

@app.route('/total', methods=['GET'])
def totalCount():
    return fetchTotalData()

@app.route("/statewise", methods=["GET"])
def statewiseCount():
    return fetchStatewiseData()

if __name__ == "__main__":
    app.run(debug=True)
