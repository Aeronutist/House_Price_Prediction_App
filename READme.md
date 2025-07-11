\# 🏡 House Price Prediction Web App – Streamlit

This project demonstrates how to turn a trained machine learning model into a fully interactive web application using \*\*Streamlit\*\*. The app allows users to input housing data and get an instant price prediction powered by a trained regression model.

\---

\## 🎯 Objective

To deploy a machine learning model that predicts California house prices based on location, income, rooms, and other features.

\---

\## 🚀 Live Preview (if deployed)

🔗 \*\[Add Streamlit Cloud link here after deployment\]\*

\---

\## 📂 Project Structure

\---

\## 💻 Tech Stack

\- \*\*Python\*\*

\- \*\*Pandas / Numpy / Scikit-learn\*\*

\- \*\*Streamlit\*\*

\- \*\*Pickle (for model serialization)\*\*

\---

\## 🧠 Features Used

| Feature | Description |

|-----------------------|-----------------------------------------|

| \`longitude\` | Geographic coordinate |

| \`latitude\` | Geographic coordinate |

| \`housing\_median\_age\` | Age of the house block |

| \`total\_rooms\` | Total rooms in the house |

| \`total\_bedrooms\` | Total bedrooms |

| \`population\` | Population in the area |

| \`households\` | Number of households |

| \`median\_income\` | Median income in area |

| \`ocean\_proximity\` | Location category (one-hot encoded) |

\---

\## 🧪 Model

\- Trained using \`LinearRegression()\` from \`sklearn\`

\- R² score, MAE, and RMSE evaluated

\- Model and Scaler saved using \`pickle\`

\---

\## 📈 App Features

\- Clean, modern Streamlit interface

\- Interactive form for user inputs

\- One-click prediction output

\- Handles categorical inputs via one-hot encoding

\---

\## ⚙️ How to Run Locally

1\. Clone the repo:

\`\`\`bash

git clone https://github.com/yourusername/House\_Price\_App.git

cd House\_Price\_App

pip install -r requirements.txt

streamlit run app.py