from flask import Flask, jsonify
import json

app = Flask(__name__)

title_list = []
json_data = open("STX Next input data.json")
jdata = json.load(json_data)



#Endpoint z listą książek
for n in range(0,10):
    title_list.append((jdata["items"][n])["volumeInfo"]["title"])
    n+=1
@app.route('/books', methods=["GET"])
def get_books_list():
    return jsonify({"tytuły książek" : title_list})

#Endpoint z lista książek z danego roku
@app.route("/books/<int:year>", methods=["GET"])
def get_sorted_by_year(year):
    choosed_books = []
    for n in range(0,10):
        if int((jdata["items"][n])["volumeInfo"]["publishedDate"]) == year:
            choosed_books.append((jdata["items"][n])["volumeInfo"]["title"])
            return jsonify({"result": choosed_books})

#Endpoint z lista książek danego autora
@app.route("/books/<first_name>/<last_name>", methods=["GET"])
def get_sorted_by_author(first_name, last_name):
    choosed_books = []
    for n in range(0,10):
        if (jdata["items"][n])["volumeInfo"]["authors"] == list(str(first_name + " " + last_name)):
            choosed_books.append((jdata["items"][n])["volumeInfo"]["title"])
            return jsonify({"result": choosed_books})

#Endpoint pokazujący dane wybranej ksiązki
@app.route("/books/<book_title>", methods=["GET"])
def get_choosed_book_info(book_title):
    for n in range(0, 10):
        if (jdata["items"][n])["volumeInfo"]["title"] == book_title:
            return jsonify({"book_info":jdata["items"][n]})


if __name__ == "__main__":
    app.run(debug=True)