# Sentiment Analysis Web Application

## Overview

A modern, powerful, and user-friendly web application for text sentiment analysis using Artificial Intelligence. This application enables you to quickly and easily analyze sentiments in various texts and view categorized results visually.


## ✨ Key Features

*   🧠 **Intelligent Sentiment Analysis:** Leveraging advanced AI models for accurate and comprehensive text sentiment analysis.
*   🎨 **Attractive and Modern UI:** Beautiful and user-friendly design with an exceptional user experience, including dark and light themes.
*   🌙 **Dark & Light Theme Support:** Choose your preferred theme for optimal usability in various lighting environments and personal preferences.
*   📊 **Categorized Result Display:** Sentiment analysis results presented in a categorized and understandable manner within the UI.
*   🚀 **High Speed & Efficiency:** Fast and optimized performance for analyzing large texts with instant responsiveness.
*   💯 **Free & Open Source:**  Project is completely free and open-source under the MIT License.

## 🛠️ Technologies Used

*   **Frontend:** HTML5, CSS3, JavaScript (ES6+)
*   **Styling Library:** [Font Awesome](https://fontawesome.com/) (for icons)
*   **Backend:** Python 3.7+, Flask (lightweight & powerful web framework)
*   **AI Library:** [Hugging Face Transformers](https://huggingface.co/transformers/) (leading NLP library)

## ⚙️ Installation & Setup Guide

Follow these steps to run the project locally or on a server:

### Prerequisites

*   [Python 3.7+](https://www.python.org/downloads/)
*   [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
*   [Node.js & npm](https://nodejs.org/) (optional, for frontend development & testing)

### Installation Steps

1.  **Get the Project Code:** Clone the GitHub repository.

    ```bash
    git clone https://github.com/miladchak/Ai-Sentiment-WebApp.git
    cd sentiment_analysis_app
    ```

2.  **Enter Backend Directory:**

    ```bash
    cd backend
    ```

3.  **Create Virtual Environment (Highly Recommended):**

    ```bash
    python -m venv venv
    ```

4.  **Activate Virtual Environment:**

    *   **Windows:** `.\venv\Scripts\activate`
    *   **Linux/macOS:** `source venv/bin/activate`

5.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (Ensure `requirements.txt` file is in the `backend` directory)

6.  **Run Flask Server:**

    ```bash
    python app.py
    ```

    The server starts at `http://127.0.0.1:5000` (local) or `http://0.0.0.0:5000` (server).

### 🌐 Accessing the Web Application

*   **Local Execution:** Open your browser and navigate to `http://127.0.0.1:5000`.
*   **Server Execution:** Open your browser and navigate to `http://<Your Server IP>:5000`. Replace `<Your Server IP>` with your server's public IP address. Ensure port 5000 is open in your server firewall.

## 💡 Usage Guide

1.  **Open Web Application:** Access the web application URL in your browser.
2.  **Enter Text:** Type or paste the text you want to analyze into the text area.
3.  **Start Analysis:** Click the "Analyze" button.
4.  **View Results:** The categorized sentiment analysis result will be displayed in the "Analysis Result" section.
5.  **Toggle Theme:** Switch website theme between dark and light mode by clicking the moon/sun icon in the header.

## 🧑‍💻 Developer

Developed with ❤️ by [Milad Chak](https://github.com/miladchak)

## 📝 License

[MIT License](LICENSE) - Free and Open Source (Optional)

---

**[مشاهده راهنمای فارسی](README.fa_IR.md)**
