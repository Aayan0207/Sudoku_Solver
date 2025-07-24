document.addEventListener("DOMContentLoaded", function () {
  const inputs = document.querySelectorAll('input[type="text"]');
  const reset = document.getElementById("reset");
  const text_string = document.getElementById("text_string");
  const sudokuForm = document.querySelector("#Sudoku-form");
  const rows = 9;
  const cols = 9;

  sudokuForm.onsubmit = (event) => {
    event.preventDefault();
    const cells = document.querySelectorAll('input[type="text"]');
    let row = 0;
    let column = 0;
    fetch("/", {
      method: "POST",
      body: new FormData(sudokuForm),
    })
      .then((response) => response.json())
      .then((data) => {
        text_string.innerHTML = data.string;
        cells.forEach((cell) => {
          if (data.answer[row][column] === 0) {
            cell.value = "";
          } else {
            cell.value = data.answer[row][column];
          }
          column += 1;
          if (column === 9) {
            row += 1;
            column = 0;
          }
        });
      })
      .catch((error) => {
        console.log(error);
      });
  };
  reset.onclick = () => {
    text_string.innerHTML =
      "Enter the unsolved sudoku. Leave cells that are to be solved blank.";
  };
  function getIndex(row, col) {
    return row * cols + col;
  }

  function getRowCol(index) {
    const row = Math.floor(index / cols);
    const col = index % cols;
    return { row, col };
  }

  function focusNextInput(row, col, key) {
    let nextRow = row;
    let nextCol = col;

    switch (key) {
      case "ArrowRight":
        nextCol = (col + 1) % cols;
        break;
      case "ArrowLeft":
        nextCol = (col - 1 + cols) % cols;
        break;
      case "ArrowDown":
        nextRow = (row + 1) % rows;
        break;
      case "ArrowUp":
        nextRow = (row - 1 + rows) % rows;
        break;
      default:
        return;
    }

    const nextIndex = getIndex(nextRow, nextCol);
    inputs[nextIndex].focus();
  }

  inputs.forEach((input, index) => {
    input.addEventListener("keydown", function (event) {
      const { row, col } = getRowCol(index);
      focusNextInput(row, col, event.key);
    });
  });
});
