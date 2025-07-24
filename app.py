from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
import sudoku
import secrets

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = 6000
app.config["SECRET_KEY"] = secrets.token_hex(16)
Session(app)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "GET":
        return render_template(
            "sudoku.html",
            answer=sudoku.null,
            string="Enter the unsolved sudoku. Leave cells that are to be solved blank.",
        )
    session["string"] = None
    session["Sudoku"] = []
    for i in range(9):
        row = []
        for j in range(9):
            if (
                request.values.get(f"cell_{i}_{j}") == ""
                or request.values.get(f"cell_{i}_{j}") == None
            ):
                row.append(0)
            else:
                try:
                    row.append(int(request.values.get(f"cell_{i}_{j}")))
                except ValueError:
                    return jsonify(
                        {
                            "answer": session["Sudoku"],
                            "string": "Invalid value given in cell.",
                        }
                    )
        session["Sudoku"].append(row)
    if len(sudoku.tosolve(session["Sudoku"])) == 81:
        session["answer"], session["string"] = (
            sudoku.null,
            "Enter the unsolved sudoku. Leave cells that are to be solved blank.",
        )
    elif sudoku.solvable(session["Sudoku"]):
        session["answer"], session["string"] = (
            sudoku.solve(session["Sudoku"]),
            "Sudoku Solved.",
        )
    else:
        session["answer"], session["string"] = session["Sudoku"], "Invalid inputs."
    return jsonify({"answer": session["answer"], "string": session["string"]})


