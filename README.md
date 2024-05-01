# Quizzy

uses Gemini to answer your google form quiz

## Installing

1. Clone the repository by

```bash
git clone https://github.com/cybersaksham/QuizGPT
```

2. Open `functions.js` and replace below line to put your OpenAI API Key which you can generate from https://platform.openai.com/account/api-keys

```js
const API_KEY = null;
```

3. Then go to `chrome://extensions/` in browser and turn on `Developer mode`

4. Click `Load Unpacked` and select the folder of the repository

5. Your extension is ready to work on `docs.google.com/forms/...` sites

## Usage

Open any google form quiz and right click the extension icon to open menu. You can also use below shortcuts to run the extension.

| Menu              | Shortcut     | Description                                                                                                                                           |
| ----------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get Answers       | Ctrl+Shift+F | It reads your quiz, find the answers and show them in the form above respective question. It also fills some multiple choice questions automatically. |
| Show/Hide Answers | Ctrl+Shift+H | It hides the answers from google form temporarily and if already hidden then show them.                                                               |
| Erase Answers     | Ctrl+Shift+E | It erases the answers data completely. You will have to press `Ctrl+Shift+F` again to find the answers                                                |
