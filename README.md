Sure! Here's a decorated and detailed GitHub main page README file:

---

# 🌟 Eclipse

Welcome to **Eclipse** by Onesmus Bett Co. 🌌 - An open-source Python module for effortless console manipulation and decoration, leveraging the power of the `rich` library.

![Eclipse](https://via.placeholder.com/800x200.png?text=Eclipse+Console+Styling)  <!-- Replace with an actual image URL -->

## 🎨 Features

- **Styled Text**: ✨ Bold, italic, underline, dim, blink, reverse, strikethrough, and reset.
- **Progress Bar**: ⏳ Customizable progress bars with ease.
- **Tables**: 📊 Beautiful tables with custom styles.
- **Panels**: 📦 Create stylish panels for displaying text.
- **Prompts**: 🔒 Input prompts with optional password masking.
- **ASCII Art**: 🎨 Generate and display stunning ASCII art.

## 🛠️ Installation

To get started with Eclipse, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/ONESMUSBETT/Eclipse.git
cd Eclipse
pip install -r requirements.txt
```

## 🚀 Usage

### 🎬 Initialization

Import the `Styled` class from the module:

```python
from eclipse import Styled
```

### 📚 Functions

#### 1. 📜 Styled.info()

Displays information about the Eclipse module and its usage.

```python
Styled.info()
```

#### 2. 📈 Styled.progress()

Displays a progress bar.

- **Params**:
  - `text`: Description text for the progress bar.
  - `color`: Color of the progress bar.
  - `font`: Font style (e.g., bold, italic, underline, dim, blink, reverse, strikethrough, reset).
  - `time_out`: Time delay between progress updates (default: 0.1).
  - `total`: Total progress value (default: 100).
  - `advance`: Incremental progress value (default: 1).

```python
Styled.progress(text="Loading", color="blue", font="bold")
```

#### 3. 🗂️ Styled.table()

Creates and displays a table.

- **Params**:
  - `title`: Title of the table.
  - `rows`: A list of lists containing row data.
  - `cols`: A list of column names.
  - `color`: Color of the table.
  - `font`: Font style.

```python
rows = [["Row 1 Col 1", "Row 1 Col 2"], ["Row 2 Col 1", "Row 2 Col 2"]]
cols = ["Column 1", "Column 2"]
Styled.table(title="Sample Table", rows=rows, cols=cols, color="green", font="bold")
```

#### 4. 📦 Styled.Box()

Creates and displays a panel (box).

- **Params**:
  - `text`: Text to display inside the panel.
  - `color`: Color of the panel.
  - `font`: Font style.

```python
Styled.Box(text="Sample Box", color="green", font="bold")
```

#### 5. 📝 Styled.inputf()

Prompts for user input.

- **Params**:
  - `text`: Prompt text.
  - `color`: Color of the prompt text.
  - `isPassWord`: Whether the input should be masked as a password (default: False).

```python
user_input = Styled.inputf(text="Enter your name:", color="white", isPassWord=False)
```

#### 6. 🖨️ Styled.printf()

Displays styled text in the console.

- **Params**:
  - `text`: Text to display.
  - `color`: Color of the text.
  - `font`: Font style.

```python
Styled.printf(text="Hello, World!", color="white", font="bold")
```

#### 7. 🅰️ Styled.ascii()

Generates and displays ASCII art.

- **Params**:
  - `text`: Text to convert to ASCII art.
  - `font`: Font style for ASCII art (e.g., r, kb, b, rt, st, sl, 3d, 4m, 5l).
  - `color`: Color of the ASCII art.

```python
ascii_art = Styled.ascii(text="Eclipse", font="3d", color="purple")
print(ascii_art)
```

## 💡 Example

Here's a small example showcasing some of the functionalities:

```python
from eclipse import Styled

Styled.info()
Styled.printf(text="This is a styled text!", color="blue", font="italic")
Styled.progress(text="Loading", color="cyan", font="bold")
Styled.Box(text="This is a box panel", color="magenta", font="bold")
ascii_art = Styled.ascii(text="Eclipse", font="5l", color="green")
print(ascii_art)
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the repository link, image URLs, and other specific details as needed to make it even more appealing.
