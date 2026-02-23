Always show details
import pypandoc

readme = r"""
# 🧠 AI Personal Health Planner

An intelligent web application that generates **personalized meal plans, workout routines, and weekly health schedules** using **LangChain + Google Gemini AI + Streamlit**.

Designed for fitness enthusiasts, students, and developers who want a smart AI-powered health planning assistant.

---

## 🚀 Features

- 🍽️ AI-generated daily meal plan (calories + macros)
- 🏋️ Personalized workout routine
- 📅 Structured 7-day health schedule
- ⚡ Parallel AI processing for fast results
- 🎛️ Interactive Streamlit UI
- 🔐 Secure API key input
- 📱 Clean and responsive interface

---

## 🖥️ Demo Preview

**Sections Generated Automatically**
- Meal Plan
- Workout Plan
- Weekly Schedule

---

## 🧰 Tech Stack

| Technology | Purpose |
|-----------|--------|
| Streamlit | Frontend UI |
| LangChain | LLM orchestration |
| Gemini API | AI generation |
| Python | Backend logic |

---

## 📦 Installation Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/ai-health-planner.git
cd ai-health-planner

2️⃣ Create Virtual Environment
Always show details
python -m venv venv

3️⃣ Activate Virtual Environment

Windows

Always show details
venv\Scripts\activate


Mac / Linux

Always show details
source venv/bin/activate

4️⃣ Install Dependencies
Always show details
pip install -r requirements.txt

5️⃣ Run Application
Always show details
streamlit run app.py

🔑 API Key Setup

When the app launches:

➡ Enter your Google Gemini API Key in the sidebar input field.

Your key is never stored — only used during runtime.

📁 Project Structure
Always show details
ai-health-planner/
│
├── app.py
├── requirements.txt
└── README.md

🎯 How It Works

User enters body + fitness info

LangChain sends prompts to Gemini

Meal + Workout generated in parallel

Weekly schedule built from results

Streamlit displays structured plans

🧪 Example Inputs
Field	Example
Age	22
Weight	70 kg
Height	170 cm
Activity	Moderate
Diet	Vegetarian
Goal	Muscle Gain
📈 Future Improvements

Progress tracking dashboard

Nutrition charts

Export plan as PDF

User login system

Dark mode

Voice assistant input

🤝 Contributing

Pull requests are welcome.

For major changes:

Fork repo

Create branch

Commit changes

Open PR

⭐ Support

If you like this project:

⭐ Star the repository
🐛 Report issues
💡 Suggest features

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

AI Health Planner Project
Built for learning + real-world AI application development.
"""