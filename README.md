<h1 align="center">🏎️ F1 AI Predictor & Analytics Dashboard</h1>

<p align="center">
A Machine Learning powered Formula 1 analytics platform that analyzes telemetry data, predicts qualifying lap times, and visualizes race performance using FastF1 and Streamlit.
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red">
<img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green">
<img src="https://img.shields.io/badge/Data-FastF1-orange">
<img src="https://img.shields.io/badge/License-MIT-yellow">
<img src="https://img.shields.io/badge/Status-Active-brightgreen">
<img src="https://img.shields.io/github/stars/berasankhadeep20-lang/F1-AI-Predictor">
<img src="https://img.shields.io/github/forks/berasankhadeep20-lang/F1-AI-Predictor">
<img src="https://img.shields.io/github/issues/berasankhadeep20-lang/F1-AI-Predictor">

</p>

---

<h2>📌 Project Overview</h2>

<p>
This project is an <b>AI-powered Formula 1 analytics system</b> that collects race data using FastF1, processes telemetry and lap data, and predicts qualifying lap performance using machine learning.
</p>

<p>
It also includes a <b>Streamlit interactive dashboard</b> for visualizing telemetry, lap comparisons, and AI predictions.
</p>

---

<h2>🚀 Features</h2>

<ul>
<li>📊 Formula 1 telemetry analysis</li>
<li>🏁 Qualifying lap time prediction using Machine Learning</li>
<li>📈 Driver lap comparison graphs</li>
<li>🚗 Speed trace visualization</li>
<li>📅 Multi-season support (2023–2025)</li>
<li>🎛 Interactive Streamlit dashboard</li>
<li>📉 AI-powered performance insights</li>
<li>⚡ FastF1 telemetry integration</li>
</ul>

---

<h2>🧠 Machine Learning Model</h2>

<p>The AI model predicts qualifying lap times using features such as:</p>

<ul>
<li>Average lap time</li>
<li>Grid position</li>
<li>Historical race data</li>
<li>Driver performance trends</li>
</ul>

<p>
The model is trained using <b>Scikit-Learn</b> and stored as a serialized model for real-time predictions.
</p>

---

<h2>📊 Dashboard Preview</h2>

<ul>
<li>Driver telemetry speed graphs</li>
<li>Lap time tables</li>
<li>Driver performance comparison</li>
<li>AI qualifying predictions</li>
</ul>

---

<h2>🛠️ Tech Stack</h2>

<ul>
<li><b>Python</b></li>
<li><b>FastF1</b> – F1 telemetry data</li>
<li><b>Scikit-Learn</b> – Machine learning</li>
<li><b>Pandas</b> – data processing</li>
<li><b>Matplotlib</b> – visualization</li>
<li><b>Streamlit</b> – dashboard interface</li>
</ul>

---

<h2>📂 Project Structure</h2>

<pre>
F1-AI-Predictor
│
├── cache/
├── data/
├── models/
│   └── f1_model.pkl
│
├── src/
│   ├── download_data.py
│   ├── process_data.py
│   ├── train_model.py
│   ├── predict_qualifying.py
│   └── lap_delta.py
│
├── dashboard.py
├── requirements.txt
├── README.md
└── LICENSE
</pre>

---

<h2>⚙️ Installation</h2>

<pre>
git clone https://github.com/berasankhadeep20-lang/F1-AI-Predictor.git

cd F1-AI-Predictor

pip install -r requirements.txt
</pre>

---

<h2>▶️ Run the Dashboard</h2>

<pre>
streamlit run dashboard.py
</pre>

The dashboard will open in your browser.

---

<h2>📈 Future Improvements</h2>

<ul>
<li>AI race strategy prediction</li>
<li>Tyre degradation modeling</li>
<li>Track map telemetry visualization</li>
<li>Full season championship simulation</li>
<li>Deep learning performance models</li>
</ul>

---

<h2>🤝 Contributing</h2>

<p>
Contributions are welcome!  
Feel free to open issues or submit pull requests.
</p>

---

<h2>📜 License</h2>

<p>This project is licensed under the MIT License.</p>

---

<p align="center">
Made with ❤️ by <b>Sankhadeep Bera</b>
</p>