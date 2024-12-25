# WhatsApp Chat Analyzer

## Project Overview
The **WhatsApp Chat Analyzer** is a Python-based tool designed to analyze and visualize WhatsApp chat data. This project provides insights such as message frequency, user activity, and common keywords, enabling users to extract meaningful patterns from their WhatsApp conversations.

---

## Features
- **Message Analysis**: Understand message trends over time.
- **User Insights**: Analyze user activity in group or personal chats.
- **Keyword Analysis**: Identify common keywords and phrases.
- **Stop Word Filtering**: Support for Hinglish stop words to clean up text data.
- **Interactive Visualizations**: View data trends and patterns through graphs.

---

## File Structure
```
WhatsApp-chat-analyzer/
├── .git/                    # Git repository
├── app.py                   # Main application script
├── helper.py                # Utility functions
├── preprocessor.py          # Data preprocessing module
├── stop_hinglish.txt        # List of Hinglish stop words
├── WhatsApp Chat with IT_elite_24hour.txt  # Sample chat data
├── WhatsApp_Chat_Dias_club.txt             # Sample chat data
├── Whats_App_Chat_Analysis.ipynb           # Jupyter Notebook for analysis
└── __pycache__/            # Compiled Python files
```

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd WhatsApp-chat-analyzer
   ```

2. **Install Dependencies**
   Ensure you have Python 3.8+ installed. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Execute the main script:
   ```bash
   python app.py
   ```

---

## Usage
1. Add your WhatsApp chat export files to the project directory.
2. Modify `app.py` or use the Jupyter Notebook to customize analysis.
3. View outputs such as graphs and statistics in the console or as generated files.

---

## Dependencies
- Python 3.8+
- Pandas
- Matplotlib
- Seaborn
- Numpy

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
Special thanks to the creators and maintainers of the libraries used in this project.

---

## Contact
For any inquiries or issues, please contact:
- **Email**: [karanmore20704@gmail.com]
