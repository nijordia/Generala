# Generala

## About This Project ℹ️
This repository contains a Python-based implementation to simulate the classic dice game **Generala** and calculate the probabilities of achieving combinations. The code allows players and developers to analyze their chances of completing specific combinations over multiple dice rolls and optimize their strategies. The project is designed to be modular, educational, and user-friendly, making it ideal for gaming enthusiasts or probability learners.

## Rules of Generala 🎲

### Objective:
Achieve one of the predefined combinations with 5 dice and score the most points over multiple rounds. Combinations include Generala, Generala Doble, Pócker, Full, Escalera, and others. The player with the highest total score at the end of all rounds wins!

### Gameplay:
1. **Initial Throw:** Roll all 5 dice at the start of your turn.
2. **Re-Rolls:** You may re-roll any or all dice up to **2 additional times** per turn.
   - After each throw, decide which dice to keep and which to re-roll.
   - After the third roll, finalize your combination or score.
3. **Combinations (Scores):**
   - **Generala Doble (100 points):** A second Generala in the same game.
   - **Generala (50 points):** Five dice of the same number.
   - **Pócker (40 points):** Four dice of the same number.
   - **Full (30 points):** Three dice of one number and two of another.
   - **Escalera (20 points):** A straight sequence (e.g., `[1, 2, 3, 4, 5]` or `[2, 3, 4, 5, 6]`).
   - **Number Scoring:** Sum of a chosen number from your dice. Example: `[2, 4, 5, 5, 6]` → Scoring **5s** gives **10 points** (2 × 5).
5. **Bonus Rule:** If you achieve a combination after your **first throw**, score an **extra 5 points**.
6. **End Of The Turn:** After your last roll, you need to match your outcome to one valid combination. If there is no valid combination left for your set of dice, you need to cross out one combination of your choice from your scoring board and you get **0 points** for this turn. 
7. **End Of The Game:** The game finishes after 11 turns. The player with the highest score wins.

## How to Contribute 🤝
Contributions are welcome! If you'd like to improve the code, add features, or fix bugs, please follow these steps:
1. **Fork the Repository:** Create a copy of this repo on your GitHub account.
2. **Create a Feature Branch:** Work on your changes in a new branch (`git checkout -b feature-name`).
3. **Test Your Changes:** Ensure your code runs correctly and integrates seamlessly with the existing implementation.
4. **Submit a Pull Request:** Open a pull request to merge your feature branch with the main branch of this repository.
5. **Follow Coding Standards:** Keep your code clean and well-documented.

Feel free to open an issue if you encounter bugs or have suggestions for improvements!

## How to Download and Run 🖥️
### Prerequisites:
- **Python:** Make sure Python is installed (recommended version: 3.8 or higher).
- **Dependencies:** Install required packages using pip.

### Steps:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nijordia/Generala.git
