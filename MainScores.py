def main_flask_function():
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route(f"/")
    @app.route(f"/home")
    def home():
        player_file = open(f"./Scores.txt", "r")
        player_score = int(player_file.read())
        print(player_score)  # TODO: remove in final version
        try:
            return render_template('home.html', player_score=player_score)
        except:
            return render_template('error.html')

    app.run()  # TODO: need to find a way to run flask in detached mode.


main_flask_function()
