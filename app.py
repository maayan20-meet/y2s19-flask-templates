from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	fav_food = ['Sushi', 'Hamburger', 'Canaloni']
	least_fav = 'abcd'
	opposite_day = True

	return render_template("index.html", foods=fav_food, day=opposite_day, least_fav=least_fav)

if __name__ == '__main__':
	app.run(debug = True)
