# **Bloom Filter: Dating App Left-Swipe Tracker**

This is a **Flask web application** that demonstrates a **Bloom filter** for tracking *left-swiped profiles* in a dating app. Users can add profile IDs (*simulating a left swipe*), check if a profile should be *shown or skipped*, and see an **animated bit array** showing how the filter works. The app also showcases a **false positive** case, where a profile *not added* might be flagged as *"skip"* due to overlapping bits.

The interface is **user-friendly**, with a **clean design**, **smooth animations**, and **clear feedback**. Built with **Python (Flask)** for the backend and **HTML/JavaScript/Tailwind CSS** for the frontend, it’s perfect for learning about **Bloom filters** in a *practical context*.

---

## **Features**

- **Add Profiles**: Simulate a *left swipe* by adding a profile ID to the Bloom filter.
- **Check Profiles**: See if a profile is *"Might be in the list—skip it!"* or *"Not in the list—show it!"*
- **Animated Bit Array**: Watch a 10x10 bit array animate as bits flip, with sequential highlights for hash positions.
- **False Positive Demo**: Test a profile (*fakeuser*) to see a possible *false positive*, with an explanation.
- **Responsive UI**: Works on desktop and mobile, with a **progress bar** and **color-coded results**.

---

## **Prerequisites**

- **Python 3.6 or higher**
- **Git** (for cloning the repository)
- A *web browser* (e.g., Chrome, Firefox)

---

## **Setup Instructions**

### **Clone the Repository**
```bash
git clone https://github.com/your-username/bloomfilter.git
cd bloomfilter
Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run the App
python3 app.py
The app will start at: http://127.0.0.1:5000
Open this URL in your browser.
Deactivate the Virtual Environment (when done)
deactivate

How to Use
Add a Profile
Enter a profile ID (e.g., Sydney Sweeney) and click "Swipe Left".
Watch the bit array animate as bits flip to 1, with hash positions highlighted.
Check a Profile
Enter the same or a new profile ID and click "Check Profile".
See the result ("show" in green or "skip" in red) with animated hash positions.
Test a False Positive
Click "Test False Positive" to check fakeuser.
If it says "skip", it’s a false positive (explained in the output).

File Structure
bash
Copy
Edit
bloomfilter/
├── app.py              # Flask backend with Bloom filter logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend with UI and animations
└── venv/               # Virtual environment (not tracked)

Dependencies
Flask: Web framework for the backend

mmh3: MurmurHash3 for hash functions

bitarray: Efficient bit array for the Bloom filter

See requirements.txt for exact versions.

## **Notes**
The Bloom filter uses 100 bits and 7 hash functions for UI visibility. Adjust size in app.py for larger filters (e.g., 1,000,000).

False positives occur with ~3% probability due to 10 preloaded profiles. Add more profiles to increase this chance.

For production, use a WSGI server (e.g., Gunicorn) and adjust the bit array size.
